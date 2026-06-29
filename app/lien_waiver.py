"""Lien-waiver type selection and state-rule lookup.

The four standard waiver types:
  1. Conditional Waiver and Release on Progress Payment
  2. Unconditional Waiver and Release on Progress Payment
  3. Conditional Waiver and Release on Final Payment
  4. Unconditional Waiver and Release on Final Payment

Selection logic (general best practice — a human verifies):
  - progress vs final  -> from payment_type
  - conditional vs unconditional -> conditional UNLESS payment has cleared
    (unconditional waivers give up lien rights even if you are not actually paid,
     so they should only be signed once funds are confirmed received/cleared).

This module never asserts a legal conclusion. Where state data is missing or a
choice is risky (e.g. an unconditional waiver before payment clears), it sets
human_review_required and explains why.
"""

from __future__ import annotations

import json
import os
from decimal import Decimal

from .models import ProjectContext, WaiverResult, PayAppResult

_RULES_PATH = os.path.join(os.path.dirname(__file__), "data", "state_lien_rules.json")

_TYPE_NAMES = {
    ("progress", True): "Conditional Waiver and Release on Progress Payment",
    ("progress", False): "Unconditional Waiver and Release on Progress Payment",
    ("final", True): "Conditional Waiver and Release on Final Payment",
    ("final", False): "Unconditional Waiver and Release on Final Payment",
}


def load_state_rules(path: str = _RULES_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def select_waiver(
    ctx: ProjectContext,
    payapp: PayAppResult | None = None,
    rules: dict | None = None,
) -> WaiverResult:
    rules = rules or load_state_rules()
    state_table = rules.get("states", {})

    payment_type = ctx.payment_type if ctx.payment_type in ("progress", "final") else "progress"
    # Explicit override wins (GCs often demand unconditional before paying);
    # otherwise default to conditional unless funds are confirmed received.
    if ctx.waiver_conditional is None:
        conditional = not ctx.payment_received
    else:
        conditional = bool(ctx.waiver_conditional)

    waiver_type = _TYPE_NAMES[(payment_type, conditional)]
    amount = payapp.line8_current_payment_due if payapp else Decimal("0")

    notes: list[str] = []
    review_reasons: list[str] = []

    # State rules
    state = ctx.state.upper().strip()
    entry = state_table.get(state)
    if entry is None:
        statutory_form = "General (no statutory form on file)"
        notarization = False
        review_reasons.append(
            f"No lien-waiver rules on file for state '{state or '(blank)'}'. "
            f"Verify whether this state mandates a statutory form / notarization."
        )
    else:
        if entry.get("statutory_forms_required"):
            statutory_form = f"{state} statutory form (per {entry.get('citation', 'state statute')})"
            notes.append(
                f"{state} mandates statutory waiver language — use the prescribed form verbatim."
            )
        else:
            statutory_form = "General (no statutory form required)"
        notarization = bool(entry.get("notarization_required"))
        for n in entry.get("notes", []):
            notes.append(n)
            if "TRAP" in n or "auto-convert" in n.lower():
                review_reasons.append(f"{state}: timing/auto-conversion rule — {n}")

    if notarization:
        notes.append("Notarization required — include a notary acknowledgment block.")

    # Risk flag: unconditional before payment clears
    if not conditional and not ctx.payment_received:
        review_reasons.append(
            "Unconditional waiver selected but payment is not confirmed received. "
            "Unconditional waivers release lien rights even if you are not paid — confirm funds cleared first."
        )

    if amount <= 0:
        review_reasons.append(
            f"Waiver amount is {amount}. A non-positive payment amount on a waiver is unusual — verify."
        )

    return WaiverResult(
        waiver_type=waiver_type,
        statutory_form=statutory_form,
        notarization_required=notarization,
        state=state,
        amount=amount,
        notes=notes,
        human_review_required=bool(review_reasons),
        review_reasons=review_reasons,
    )
