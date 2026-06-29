import unittest
from decimal import Decimal

from app.models import ProjectContext
from app.payapp import compute_pay_application

SAMPLE = {
    "project_name": "Test",
    "state": "CA",
    "period_through": "2026-06-30",
    "original_contract_sum": 150000,
    "retainage_pct": 10,
    "previous_certificates": 36000,
    "line_items": [
        {"item_no": "1", "description": "Rough-in", "scheduled_value": 100000,
         "previous_completed": 40000, "this_period_completed": 20000, "materials_stored": 0},
        {"item_no": "2", "description": "Fixtures", "scheduled_value": 50000,
         "previous_completed": 10000, "this_period_completed": 10000, "materials_stored": 5000},
    ],
}


class TestPayApp(unittest.TestCase):
    def setUp(self):
        self.ctx = ProjectContext.from_dict(SAMPLE)
        self.r = compute_pay_application(self.ctx)

    def test_line_item_totals(self):
        i1, i2 = self.r.line_results
        self.assertEqual(i1.total_completed_stored, Decimal("60000.00"))
        self.assertEqual(i1.balance_to_finish, Decimal("40000.00"))
        self.assertEqual(i2.total_completed_stored, Decimal("25000.00"))
        self.assertEqual(i2.balance_to_finish, Decimal("25000.00"))

    def test_percent(self):
        i1, i2 = self.r.line_results
        self.assertEqual(round(i1.percent, 2), Decimal("0.60"))
        self.assertEqual(round(i2.percent, 2), Decimal("0.50"))

    def test_g702_lines(self):
        r = self.r
        self.assertEqual(r.line1_original_contract, Decimal("150000.00"))
        self.assertEqual(r.line2_net_change_orders, Decimal("0.00"))
        self.assertEqual(r.line3_contract_sum_to_date, Decimal("150000.00"))
        self.assertEqual(r.line4_total_completed_stored, Decimal("85000.00"))
        self.assertEqual(r.line5a_retainage_work, Decimal("8000.00"))
        self.assertEqual(r.line5b_retainage_stored, Decimal("500.00"))
        self.assertEqual(r.line5_retainage, Decimal("8500.00"))
        self.assertEqual(r.line6_total_earned_less_retainage, Decimal("76500.00"))
        self.assertEqual(r.line7_previous_certificates, Decimal("36000.00"))
        self.assertEqual(r.line8_current_payment_due, Decimal("40500.00"))
        self.assertEqual(r.line9_balance_to_finish_incl_retainage, Decimal("73500.00"))

    def test_change_order_flows_to_line3(self):
        data = dict(SAMPLE, change_orders=[{"description": "Add panel", "amount": 10000}])
        r = compute_pay_application(ProjectContext.from_dict(data))
        self.assertEqual(r.line2_net_change_orders, Decimal("10000.00"))
        self.assertEqual(r.line3_contract_sum_to_date, Decimal("160000.00"))

    def test_no_float_artifacts(self):
        # 0.1-style retainage must not introduce binary-float drift.
        data = dict(SAMPLE, retainage_pct=10)
        r = compute_pay_application(ProjectContext.from_dict(data))
        self.assertEqual(r.line5_retainage, Decimal("8500.00"))


if __name__ == "__main__":
    unittest.main()
