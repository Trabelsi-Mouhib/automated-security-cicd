import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host")
    # VULNÉRABILITÉ : Injection de commande système (OS Command Injection)
    # Un attaquant pourrait passer : 127.0.0.1; cat /etc/passwd
    output = os.popen(f"ping -c 1 {host}").read()
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)