import unittest
from decimal import Decimal

from app.models import ProjectContext
from app.payapp import compute_pay_application
from app.lien_waiver import select_waiver

BASE = {
    "project_name": "Test",
    "state": "CA",
    "period_through": "2026-06-30",
    "original_contract_sum": 100000,
    "retainage_pct": 10,
    "previous_certificates": 0,
    "line_items": [
        {"item_no": "1", "scheduled_value": 100000,
         "previous_completed": 0, "this_period_completed": 50000, "materials_stored": 0},
    ],
}


def waiver_for(**overrides):
    data = dict(BASE, **overrides)
    ctx = ProjectContext.from_dict(data)
    return select_waiver(ctx, compute_pay_application(ctx))


class TestLienWaiver(unittest.TestCase):
    def test_ca_conditional_progress_default(self):
        w = waiver_for(state="CA")
        self.assertEqual(w.waiver_type, "Conditional Waiver and Release on Progress Payment")
        self.assertIn("CA statutory form", w.statutory_form)
        self.assertFalse(w.notarization_required)

    def test_final_payment_type(self):
        w = waiver_for(payment_type="final", payment_received=True)
        self.assertEqual(w.waiver_type, "Unconditional Waiver and Release on Final Payment")

    def test_tx_requires_notarization(self):
        w = waiver_for(state="TX")
        self.assertTrue(w.notarization_required)

    def test_ga_timing_trap_flags_review(self):
        w = waiver_for(state="GA")
        self.assertTrue(w.human_review_required)
        self.assertTrue(any("GA" in r for r in w.review_reasons))

    def test_unknown_state_flags_review(self):
        w = waiver_for(state="ZZ")
        self.assertTrue(w.human_review_required)
        self.assertIn("General", w.statutory_form)

    def test_unconditional_before_payment_flags_review(self):
        # GC demands unconditional but funds not confirmed -> risky, must flag.
        w = waiver_for(state="CA", waiver_conditional=False, payment_received=False)
        self.assertEqual(w.waiver_type, "Unconditional Waiver and Release on Progress Payment")
        self.assertTrue(w.human_review_required)
        self.assertTrue(any("not confirmed" in r.lower() or "cleared" in r.lower()
                            for r in w.review_reasons))

    def test_amount_matches_payment_due(self):
        ctx = ProjectContext.from_dict(BASE)
        a = compute_pay_application(ctx)
        w = select_waiver(ctx, a)
        self.assertEqual(w.amount, a.line8_current_payment_due)
        self.assertEqual(w.amount, Decimal("45000.00"))  # 50000 - 10% retainage


if __name__ == "__main__":
    unittest.main()
