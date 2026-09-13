from flask import Flask, request
import sqlite3

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded Secret Token (Triggers TruffleHog)
SLACK_TOKEN = "xoxb-123456789012-1234567890123-456789012345678901234567"

@app.route("/user")
def get_user_data():
    username = request.args.get("username")
    # VULNERABILITY 2: SQL Injection (Triggers Semgrep)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchall()

@app.route("/calc")
def run_calculator():
    user_input = request.args.get("calc")
    # VULNERABILITY 3: Unsafe Eval / RCE (Triggers Semgrep)
    return eval(user_input)