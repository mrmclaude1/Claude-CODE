"""Typed inputs/outputs for the pay-app + lien-waiver engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .money import money, pct


@dataclass
class LineItem:
    """One row of the Schedule of Values (AIA G703)."""
    item_no: str
    description: str
    scheduled_value: Decimal
    previous_completed: Decimal = Decimal("0")   # col D
    this_period_completed: Decimal = Decimal("0") # col E
    materials_stored: Decimal = Decimal("0")      # col F (not in D or E)

    @classmethod
    def from_dict(cls, d: dict) -> "LineItem":
        return cls(
            item_no=str(d["item_no"]),
            description=str(d.get("description", "")),
            scheduled_value=money(d["scheduled_value"]),
            previous_completed=money(d.get("previous_completed", 0)),
            this_period_completed=money(d.get("this_period_completed", 0)),
            materials_stored=money(d.get("materials_stored", 0)),
        )


@dataclass
class ChangeOrder:
    description: str
    amount: Decimal  # net (may be negative)

    @classmethod
    def from_dict(cls, d: dict) -> "ChangeOrder":
        return cls(description=str(d.get("description", "")), amount=money(d["amount"]))


@dataclass
class ProjectContext:
    """Everything the engine needs about a single pay application."""
    project_name: str
    state: str                       # 2-letter US state code (waiver rules)
    period_through: str              # billing period end date, e.g. "2026-06-30"
    original_contract_sum: Decimal
    line_items: list[LineItem]
    change_orders: list[ChangeOrder] = field(default_factory=list)
    retainage_pct_work: Decimal = Decimal("0.10")    # on completed work (D+E)
    retainage_pct_stored: Decimal = Decimal("0.10")  # on stored materials (F)
    # AIA G702 line 7: the prior application's "total earned less retainage" (line 6).
    previous_certificates: Decimal = Decimal("0")
    # Payment context for waiver selection:
    payment_type: str = "progress"   # "progress" | "final"
    payment_received: bool = False    # drives conditional vs unconditional
    # Optional explicit override (GCs often DEMAND unconditional before paying).
    # None -> derive from payment_received; True -> conditional; False -> unconditional.
    waiver_conditional: Optional[bool] = None

    @classmethod
    def from_dict(cls, d: dict) -> "ProjectContext":
        return cls(
            project_name=str(d.get("project_name", "")),
            state=str(d.get("state", "")).upper().strip(),
            period_through=str(d.get("period_through", "")),
            original_contract_sum=money(d["original_contract_sum"]),
            line_items=[LineItem.from_dict(x) for x in d["line_items"]],
            change_orders=[ChangeOrder.from_dict(x) for x in d.get("change_orders", [])],
            retainage_pct_work=pct(d.get("retainage_pct_work", d.get("retainage_pct", 0.10))),
            retainage_pct_stored=pct(d.get("retainage_pct_stored", d.get("retainage_pct", 0.10))),
            previous_certificates=money(d.get("previous_certificates", 0)),
            payment_type=str(d.get("payment_type", "progress")).lower().strip(),
            payment_received=bool(d.get("payment_received", False)),
            waiver_conditional=d.get("waiver_conditional", None),
        )


@dataclass
class LineItemResult:
    item_no: str
    description: str
    scheduled_value: Decimal
    previous_completed: Decimal
    this_period_completed: Decimal
    materials_stored: Decimal
    total_completed_stored: Decimal  # col G = D+E+F
    percent: Decimal                 # G/C
    balance_to_finish: Decimal       # C-G


@dataclass
class PayAppResult:
    """AIA G702/G703 computed figures."""
    line_results: list[LineItemResult]
    # G702 lines:
    line1_original_contract: Decimal
    line2_net_change_orders: Decimal
    line3_contract_sum_to_date: Decimal
    line4_total_completed_stored: Decimal
    line5_retainage: Decimal
    line5a_retainage_work: Decimal
    line5b_retainage_stored: Decimal
    line6_total_earned_less_retainage: Decimal
    line7_previous_certificates: Decimal
    line8_current_payment_due: Decimal
    line9_balance_to_finish_incl_retainage: Decimal


@dataclass
class WaiverResult:
    waiver_type: str            # e.g. "Conditional Waiver and Release on Progress Payment"
    statutory_form: str         # form name or "General (no statutory form)"
    notarization_required: bool
    state: str
    amount: Decimal             # "through" / payment amount on the waiver
    notes: list[str] = field(default_factory=list)
    human_review_required: bool = False
    review_reasons: list[str] = field(default_factory=list)


@dataclass
class ComplianceFlag:
    severity: str   # "ERROR" | "WARNING" | "INFO"
    code: str
    message: str


@dataclass
class DraftPackage:
    project: ProjectContext
    payapp: PayAppResult
    waiver: WaiverResult
    flags: list[ComplianceFlag]
    final: bool = False   # always False from this engine — humans finalize
