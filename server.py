from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "leads.db"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def init_db() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.commit()


class LeadHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_POST(self) -> None:
        if self.path != "/api/leads":
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return

        content_length = self.headers.get("Content-Length")
        if content_length is None:
            self._send_json({"error": "Missing request body."}, HTTPStatus.BAD_REQUEST)
            return

        try:
            raw_body = self.rfile.read(int(content_length))
            payload = json.loads(raw_body.decode("utf-8"))
        except (ValueError, json.JSONDecodeError):
            self._send_json({"error": "Invalid JSON payload."}, HTTPStatus.BAD_REQUEST)
            return

        name = str(payload.get("name", "")).strip()
        email = str(payload.get("email", "")).strip().lower()

        if not name:
            self._send_json({"error": "Please enter your name."}, HTTPStatus.BAD_REQUEST)
            return

        if not email or not EMAIL_RE.match(email):
            self._send_json(
                {"error": "Please enter a valid email address."},
                HTTPStatus.BAD_REQUEST,
            )
            return

        created_at = datetime.now(timezone.utc).isoformat()

        with sqlite3.connect(DB_PATH) as connection:
            connection.execute(
                "INSERT INTO leads (name, email, created_at) VALUES (?, ?, ?)",
                (name, email, created_at),
            )
            connection.commit()

        self._send_json({"ok": True}, HTTPStatus.CREATED)

    def _send_json(self, payload: dict[str, object], status: HTTPStatus) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    init_db()
    server = ThreadingHTTPServer(("127.0.0.1", 4173), LeadHandler)
    print(f"Serving Links AI at http://127.0.0.1:4173 using database {DB_PATH}")
    server.serve_forever()
