from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de données fictive
ITEMS = [
    {"id": 1, "name": "Serveur Web", "status": "actif"},
    {"id": 2, "name": "Base de données", "status": "actif"},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "API DevSecOps opérationnelle"}), 200

@app.route("/api/items", methods=["GET"])
def get_items():
    search = request.args.get("search", "").lower()
    if search:
        filtered = [i for i in ITEMS if search in i["name"].lower()]
        return jsonify(filtered), 200
    return jsonify(ITEMS), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)