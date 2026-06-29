"""Minimal HTTP service exposing the deterministic core engine.

Pure standard library — no Flask/FastAPI, no dependencies. This is what n8n
(on your Unraid server) calls over HTTP instead of shelling out.

Endpoints:
  GET  /health  -> {"status": "ok"}
  POST /draft   -> body: a ProjectContext JSON  ->  draft package JSON
                   (includes g702 lines, waiver, compliance flags, markdown)

Run:
  python3 -m app.server                  # listens on 0.0.0.0:8000
  PORT=9000 python3 -m app.server        # custom port

Every response is a DRAFT and sets requires_human_qa=true. Nothing is finalized
or sent here — the human QA gate lives downstream (see automation/README.md).
"""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .models import ProjectContext
from .pipeline import build_draft_package, package_to_dict

MAX_BODY = 2 * 1024 * 1024  # 2 MB cap on request bodies


class Handler(BaseHTTPRequestHandler):
    server_version = "PayAppEngine/1.0"

    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path.rstrip("/") in ("/health", ""):
            self._send(200, {"status": "ok", "service": "payapp-engine"})
        else:
            self._send(404, {"error": "not found", "path": self.path})

    def do_POST(self) -> None:
        if self.path.rstrip("/") != "/draft":
            self._send(404, {"error": "not found", "path": self.path})
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
        except ValueError:
            self._send(400, {"error": "invalid Content-Length"})
            return
        if length <= 0:
            self._send(400, {"error": "empty body; POST a ProjectContext JSON"})
            return
        if length > MAX_BODY:
            self._send(413, {"error": "body too large"})
            return

        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            self._send(400, {"error": f"invalid JSON: {exc}"})
            return

        try:
            ctx = ProjectContext.from_dict(data)
            pkg = build_draft_package(ctx)
        except (KeyError, ValueError, TypeError) as exc:
            # Bad input -> 422, with the reason, rather than a 500.
            self._send(422, {"error": f"could not build package: {exc}"})
            return

        self._send(200, package_to_dict(pkg))

    def log_message(self, fmt: str, *args) -> None:  # quieter logs
        # Route access logs to stderr in a compact form.
        import sys
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main() -> None:
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    httpd = ThreadingHTTPServer((host, port), Handler)
    print(f"payapp-engine listening on http://{host}:{port}  (POST /draft, GET /health)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("shutting down")
        httpd.shutdown()


if __name__ == "__main__":
    main()
