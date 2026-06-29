"""AIA G702/G703 computation.

Standard AIA G703 continuation columns per line item:
  C  Scheduled Value
  D  Work completed from previous applications
  E  Work completed this period
  F  Materials presently stored (not in D or E)
  G  Total completed and stored to date = D + E + F
  %  G / C
  H  Balance to finish = C - G

Standard AIA G702 lines:
  1  Original contract sum
  2  Net change by change orders
  3  Contract sum to date = 1 +/- 2
  4  Total completed & stored to date = sum of column G
  5  Retainage:  a) % of completed work (D+E)  +  b) % of stored material (F)
  6  Total earned less retainage = 4 - 5
  7  Less previous certificates for payment (line 6 from prior application)
  8  Current payment due = 6 - 7
  9  Balance to finish including retainage = 3 - 6
"""

from __future__ import annotations

from decimal import Decimal

from .models import ProjectContext, PayAppResult, LineItemResult
from .money import money


def compute_pay_application(ctx: ProjectContext) -> PayAppResult:
    line_results: list[LineItemResult] = []

    total_scheduled = Decimal("0")
    total_g = Decimal("0")
    total_completed_work = Decimal("0")  # D+E across all lines (for retainage a)
    total_stored = Decimal("0")          # F across all lines (for retainage b)

    for li in ctx.line_items:
        g = money(li.previous_completed + li.this_period_completed + li.materials_stored)
        balance = money(li.scheduled_value - g)
        percent = (
            (g / li.scheduled_value) if li.scheduled_value != 0 else Decimal("0")
        )
        line_results.append(
            LineItemResult(
                item_no=li.item_no,
                description=li.description,
                scheduled_value=li.scheduled_value,
                previous_completed=li.previous_completed,
                this_period_completed=li.this_period_completed,
                materials_stored=li.materials_stored,
                total_completed_stored=g,
                percent=percent,
                balance_to_finish=balance,
            )
        )
        total_scheduled += li.scheduled_value
        total_g += g
        total_completed_work += li.previous_completed + li.this_period_completed
        total_stored += li.materials_stored

    line1 = ctx.original_contract_sum
    line2 = money(sum((co.amount for co in ctx.change_orders), Decimal("0")))
    line3 = money(line1 + line2)
    line4 = money(total_g)

    retainage_work = money(ctx.retainage_pct_work * total_completed_work)
    retainage_stored = money(ctx.retainage_pct_stored * total_stored)
    line5 = money(retainage_work + retainage_stored)

    line6 = money(line4 - line5)
    line7 = ctx.previous_certificates
    line8 = money(line6 - line7)
    line9 = money(line3 - line6)

    return PayAppResult(
        line_results=line_results,
        line1_original_contract=line1,
        line2_net_change_orders=line2,
        line3_contract_sum_to_date=line3,
        line4_total_completed_stored=line4,
        line5_retainage=line5,
        line5a_retainage_work=retainage_work,
        line5b_retainage_stored=retainage_stored,
        line6_total_earned_less_retainage=line6,
        line7_previous_certificates=line7,
        line8_current_payment_due=line8,
        line9_balance_to_finish_incl_retainage=line9,
    )
