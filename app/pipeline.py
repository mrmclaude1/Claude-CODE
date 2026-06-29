"""Orchestrates the deterministic core into a single DRAFT package.

build_draft_package(ctx) -> DraftPackage
render_markdown(package) -> str   (human-readable, marked NOT FINAL)

This is the unit n8n calls after the LLM has extracted structured data and
before the human QA gate. Nothing here finalizes or sends anything.
"""

from __future__ import annotations

from .models import ProjectContext, DraftPackage, ComplianceFlag
from .payapp import compute_pay_application
from .lien_waiver import select_waiver
from .compliance import run_compliance_checks
from .money import fmt

_BANNER = "NOT FINAL — DRAFT PENDING HUMAN QA"


def build_draft_package(ctx: ProjectContext) -> DraftPackage:
    payapp = compute_pay_application(ctx)
    waiver = select_waiver(ctx, payapp)
    flags = run_compliance_checks(ctx, payapp, waiver)
    return DraftPackage(project=ctx, payapp=payapp, waiver=waiver, flags=flags, final=False)


def has_blocking_errors(flags: list[ComplianceFlag]) -> bool:
    return any(f.severity == "ERROR" for f in flags)


def package_to_dict(pkg: DraftPackage) -> dict:
    """JSON-serializable view of a draft package (Decimals -> strings)."""
    a, w = pkg.payapp, pkg.waiver
    return {
        "requires_human_qa": True,
        "final": pkg.final,  # always False from this engine
        "blocking_errors": has_blocking_errors(pkg.flags),
        "project": {
            "project_name": pkg.project.project_name,
            "state": pkg.project.state,
            "period_through": pkg.project.period_through,
        },
        "g702": {
            "line1_original_contract": str(a.line1_original_contract),
            "line2_net_change_orders": str(a.line2_net_change_orders),
            "line3_contract_sum_to_date": str(a.line3_contract_sum_to_date),
            "line4_total_completed_stored": str(a.line4_total_completed_stored),
            "line5_retainage": str(a.line5_retainage),
            "line6_total_earned_less_retainage": str(a.line6_total_earned_less_retainage),
            "line7_previous_certificates": str(a.line7_previous_certificates),
            "line8_current_payment_due": str(a.line8_current_payment_due),
            "line9_balance_to_finish_incl_retainage": str(a.line9_balance_to_finish_incl_retainage),
        },
        "waiver": {
            "waiver_type": w.waiver_type,
            "statutory_form": w.statutory_form,
            "notarization_required": w.notarization_required,
            "amount": str(w.amount),
            "notes": w.notes,
            "human_review_required": w.human_review_required,
            "review_reasons": w.review_reasons,
        },
        "flags": [
            {"severity": f.severity, "code": f.code, "message": f.message}
            for f in pkg.flags
        ],
        "markdown": render_markdown(pkg),
    }


def render_markdown(pkg: DraftPackage) -> str:
    p, a, w = pkg.project, pkg.payapp, pkg.waiver
    lines: list[str] = []
    out = lines.append

    out(f"# {_BANNER}")
    out("")
    out(f"**Project:** {p.project_name}  |  **State:** {p.state}  |  **Through:** {p.period_through}")
    out("")

    # G703
    out("## G703 — Continuation Sheet (DRAFT)")
    out("")
    out("| Item | Description | Scheduled (C) | Prev (D) | This Period (E) | Stored (F) | Completed+Stored (G) | % | Balance (H) |")
    out("|---|---|--:|--:|--:|--:|--:|--:|--:|")
    for lr in a.line_results:
        out(
            f"| {lr.item_no} | {lr.description} | {fmt(lr.scheduled_value)} | "
            f"{fmt(lr.previous_completed)} | {fmt(lr.this_period_completed)} | "
            f"{fmt(lr.materials_stored)} | {fmt(lr.total_completed_stored)} | "
            f"{lr.percent * 100:.1f}% | {fmt(lr.balance_to_finish)} |"
        )
    out("")

    # G702
    out("## G702 — Application and Certificate for Payment (DRAFT)")
    out("")
    out("| Line | Description | Amount |")
    out("|---|---|--:|")
    out(f"| 1 | Original contract sum | {fmt(a.line1_original_contract)} |")
    out(f"| 2 | Net change by change orders | {fmt(a.line2_net_change_orders)} |")
    out(f"| 3 | Contract sum to date | {fmt(a.line3_contract_sum_to_date)} |")
    out(f"| 4 | Total completed & stored to date | {fmt(a.line4_total_completed_stored)} |")
    out(f"| 5a | Retainage on completed work | {fmt(a.line5a_retainage_work)} |")
    out(f"| 5b | Retainage on stored material | {fmt(a.line5b_retainage_stored)} |")
    out(f"| 5 | Total retainage | {fmt(a.line5_retainage)} |")
    out(f"| 6 | Total earned less retainage | {fmt(a.line6_total_earned_less_retainage)} |")
    out(f"| 7 | Less previous certificates | {fmt(a.line7_previous_certificates)} |")
    out(f"| **8** | **Current payment due** | **{fmt(a.line8_current_payment_due)}** |")
    out(f"| 9 | Balance to finish incl. retainage | {fmt(a.line9_balance_to_finish_incl_retainage)} |")
    out("")

    # Waiver
    out("## Lien Waiver (DRAFT)")
    out("")
    out(f"- **Type:** {w.waiver_type}")
    out(f"- **Form:** {w.statutory_form}")
    out(f"- **Amount:** {fmt(w.amount)}")
    out(f"- **Notarization required:** {'YES' if w.notarization_required else 'no'}")
    if w.notes:
        out("- **Notes:**")
        for n in w.notes:
            out(f"  - {n}")
    out("")

    # Compliance
    out("## ⚠️ Compliance flags for human review")
    out("")
    order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
    icon = {"ERROR": "🔴", "WARNING": "🟡", "INFO": "⚪"}
    for f in sorted(pkg.flags, key=lambda x: order.get(x.severity, 9)):
        out(f"- {icon.get(f.severity, '')} **{f.severity}** [{f.code}] {f.message}")
    out("")
    if has_blocking_errors(pkg.flags):
        out("> 🔴 **BLOCKING ERRORS present — do not ship until resolved.**")
    else:
        out("> No blocking errors. **Human QA still required** before this package is submitted.")
    out("")
    out(f"_{_BANNER}_")
    return "\n".join(lines)
