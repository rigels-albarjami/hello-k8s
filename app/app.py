import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello from Kubernetes!")
    hostname = socket.gethostname()
    return f"""
    <html>
      <head><title>hello-k8s</title></head>
      <body style="font-family: sans-serif; text-align: center; margin-top: 15%;">
        <h1>{message}</h1>
        <p>Served by: <b>{hostname}</b></p>
        <p>Version: {APP_VERSION}</p>
      </body>
    </html>
    """


@app.route("/healthz")
def healthz():
    return jsonify(status="ok")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)