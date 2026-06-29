import json
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

from app.server import Handler

SAMPLE = {
    "project_name": "Server Test",
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


class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def _request(self, method, path, body=None):
        conn = HTTPConnection("127.0.0.1", self.port, timeout=5)
        payload = json.dumps(body).encode() if body is not None else None
        headers = {"Content-Type": "application/json"} if payload else {}
        conn.request(method, path, body=payload, headers=headers)
        resp = conn.getresponse()
        data = json.loads(resp.read().decode())
        conn.close()
        return resp.status, data

    def test_health(self):
        status, data = self._request("GET", "/health")
        self.assertEqual(status, 200)
        self.assertEqual(data["status"], "ok")

    def test_draft_happy_path(self):
        status, data = self._request("POST", "/draft", SAMPLE)
        self.assertEqual(status, 200)
        self.assertTrue(data["requires_human_qa"])
        self.assertFalse(data["final"])
        self.assertEqual(data["g702"]["line8_current_payment_due"], "40500.00")
        self.assertIn("NOT FINAL", data["markdown"])

    def test_draft_bad_json(self):
        conn = HTTPConnection("127.0.0.1", self.port, timeout=5)
        conn.request("POST", "/draft", body=b"{not json", headers={"Content-Type": "application/json"})
        resp = conn.getresponse()
        self.assertEqual(resp.status, 400)
        conn.close()

    def test_draft_missing_field(self):
        bad = {"project_name": "x"}  # missing required fields
        status, data = self._request("POST", "/draft", bad)
        self.assertEqual(status, 422)
        self.assertIn("error", data)

    def test_unknown_route(self):
        status, _ = self._request("GET", "/nope")
        self.assertEqual(status, 404)


if __name__ == "__main__":
    unittest.main()
