import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. FAILLE SECRETS (TruffleHog) : Clé API Slack valide/exposée en dur
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "vulnerable"}), 200

# 2. FAILLE SAST (Semgrep) : Injection de commande système via os.system()
@app.route("/api/ping", methods=["GET"])
def ping_host():
    target = request.args.get("host", "127.0.0.1")
    # Injection possible : ?host=127.0.0.1;cat /etc/passwd
    cmd = f"ping -c 1 {target}"
    os.system(cmd) 
    return jsonify({"msg": f"Ping envoyé à {target}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)