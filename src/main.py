import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from .login_service import LoginService

service = LoginService()


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {"status": "UP"})
        else:
            self.send_json(404, {"error": "Not found"})

    def do_POST(self):
        if self.path != "/login":
            self.send_json(404, {"error": "Not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            email = data["email"]
            password = data["password"]
            success, message = service.login(email, password)
            self.send_json(200, {"success": success, "message": message})
        except (ValueError, KeyError, json.JSONDecodeError):
            self.send_json(400, {"error": "Invalid JSON or missing credentials"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"SmartCampus démarre sur le port {port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()