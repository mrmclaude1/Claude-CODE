import unittest
from decimal import Decimal

from app.models import ProjectContext, WaiverResult
from app.payapp import compute_pay_application
from app.lien_waiver import select_waiver
from app.compliance import run_compliance_checks
from app.pipeline import build_draft_package, has_blocking_errors

CLEAN = {
    "project_name": "Test",
    "state": "CA",
    "period_through": "2026-06-30",
    "original_contract_sum": 150000,
    "retainage_pct": 10,
    "previous_certificates": 36000,
    "line_items": [
        {"item_no": "1", "scheduled_value": 100000,
         "previous_completed": 40000, "this_period_completed": 20000, "materials_stored": 0},
        {"item_no": "2", "scheduled_value": 50000,
         "previous_completed": 10000, "this_period_completed": 10000, "materials_stored": 5000},
    ],
}


def codes(flags):
    return {f.code for f in flags}


def run(data):
    ctx = ProjectContext.from_dict(data)
    a = compute_pay_application(ctx)
    w = select_waiver(ctx, a)
    return run_compliance_checks(ctx, a, w)


class TestCompliance(unittest.TestCase):
    def test_clean_package_has_no_errors(self):
        pkg = build_draft_package(ProjectContext.from_dict(CLEAN))
        self.assertFalse(has_blocking_errors(pkg.flags))

    def test_sov_contract_mismatch(self):
        # Change order raises contract sum but SOV unchanged -> mismatch error.
        data = dict(CLEAN, change_orders=[{"description": "extra", "amount": 10000}])
        self.assertIn("SOV_CONTRACT_MISMATCH", codes(run(data)))

    def test_overbilling_detected(self):
        data = dict(CLEAN)
        data["line_items"] = [
            {"item_no": "1", "scheduled_value": 100000,
             "previous_completed": 90000, "this_period_completed": 20000, "materials_stored": 0},
            {"item_no": "2", "scheduled_value": 50000,
             "previous_completed": 10000, "this_period_completed": 10000, "materials_stored": 5000},
        ]
        self.assertIn("OVERBILL", codes(run(data)))

    def test_negative_payment(self):
        data = dict(CLEAN, previous_certificates=200000)
        self.assertIn("NEGATIVE_PAYMENT", codes(run(data)))

    def test_missing_period(self):
        data = dict(CLEAN, period_through="")
        self.assertIn("MISSING_PERIOD", codes(run(data)))

    def test_waiver_amount_mismatch(self):
        ctx = ProjectContext.from_dict(CLEAN)
        a = compute_pay_application(ctx)
        bad_waiver = WaiverResult(
            waiver_type="x", statutory_form="x", notarization_required=False,
            state="CA", amount=Decimal("999.00"),
        )
        self.assertIn("WAIVER_AMOUNT_MISMATCH", codes(run_compliance_checks(ctx, a, bad_waiver)))


if __name__ == "__main__":
    unittest.main()
