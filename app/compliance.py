"""Deterministic compliance checks on a computed pay application + waiver.

These catch the errors that delay payment or create liability: math that does
not reconcile, over-billing, negative payment due, retainage drift, missing
period/date, and waiver/pay-app amount mismatch. ERRORs must be resolved before
the package ships; WARNINGs need human eyes.
"""

from __future__ import annotations

from decimal import Decimal

from .models import (
    ProjectContext,
    PayAppResult,
    WaiverResult,
    ComplianceFlag,
)

_TOLERANCE = Decimal("0.01")  # one cent


def run_compliance_checks(
    ctx: ProjectContext,
    payapp: PayAppResult,
    waiver: WaiverResult,
) -> list[ComplianceFlag]:
    flags: list[ComplianceFlag] = []

    def err(code, msg):
        flags.append(ComplianceFlag("ERROR", code, msg))

    def warn(code, msg):
        flags.append(ComplianceFlag("WARNING", code, msg))

    def info(code, msg):
        flags.append(ComplianceFlag("INFO", code, msg))

    # 1. Contract sum to date should equal the sum of scheduled values.
    total_scheduled = sum((li.scheduled_value for li in payapp.line_results), Decimal("0"))
    if abs(total_scheduled - payapp.line3_contract_sum_to_date) > _TOLERANCE:
        err(
            "SOV_CONTRACT_MISMATCH",
            f"Sum of scheduled values ({total_scheduled}) != contract sum to date "
            f"(line 3 = {payapp.line3_contract_sum_to_date}). Approved change orders may be "
            f"missing from the Schedule of Values, or vice versa.",
        )

    # 2. No line item over-billed (G must not exceed scheduled value).
    for lr in payapp.line_results:
        if lr.total_completed_stored - lr.scheduled_value > _TOLERANCE:
            err(
                "OVERBILL",
                f"Item {lr.item_no} billed {lr.total_completed_stored} against a scheduled value "
                f"of {lr.scheduled_value} (over by "
                f"{lr.total_completed_stored - lr.scheduled_value}).",
            )

    # 3. Current payment due should not be negative.
    if payapp.line8_current_payment_due < 0:
        err(
            "NEGATIVE_PAYMENT",
            f"Current payment due (line 8) is negative: {payapp.line8_current_payment_due}. "
            f"Previous certificates ({payapp.line7_previous_certificates}) may exceed earned-less-retainage.",
        )

    # 4. Retainage sanity: line 6 + line 5 should equal line 4.
    if abs((payapp.line6_total_earned_less_retainage + payapp.line5_retainage)
           - payapp.line4_total_completed_stored) > _TOLERANCE:
        err(
            "RETAINAGE_MATH",
            "Earned-less-retainage (line 6) + retainage (line 5) != total completed & stored (line 4).",
        )

    # 5. Balance to finish should be non-negative.
    if payapp.line9_balance_to_finish_incl_retainage < -_TOLERANCE:
        warn(
            "NEGATIVE_BALANCE",
            f"Balance to finish (line 9) is negative: "
            f"{payapp.line9_balance_to_finish_incl_retainage}. Possible over-billing or contract-sum error.",
        )

    # 6. Period / date present.
    if not ctx.period_through.strip():
        err("MISSING_PERIOD", "Billing period 'through' date is missing.")

    # 7. Waiver amount should match current payment due.
    if abs(waiver.amount - payapp.line8_current_payment_due) > _TOLERANCE:
        err(
            "WAIVER_AMOUNT_MISMATCH",
            f"Lien-waiver amount ({waiver.amount}) does not match current payment due "
            f"(line 8 = {payapp.line8_current_payment_due}).",
        )

    # 8. Surface waiver review reasons as compliance flags.
    if waiver.human_review_required:
        for reason in waiver.review_reasons:
            warn("WAIVER_REVIEW", reason)

    # 9. Notarization reminder.
    if waiver.notarization_required:
        info("NOTARY", f"{waiver.state}: notarization required — include a notary block.")

    if not flags:
        info("CLEAN", "No automated compliance issues detected. Human QA still required.")

    return flags
