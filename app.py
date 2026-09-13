import os
import ast
from flask import Flask, request
import sqlite3

app = Flask(__name__)

# FIX 1: Read secrets from environment variables instead of hardcoding
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

@app.route("/user")
def get_user_data():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # FIX 2: Use parameterized queries (?) to block SQL Injection
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()

@app.route("/calc")
def run_calculator():
    user_input = request.args.get("calc")
    # FIX 3: Use ast.literal_eval to eliminate Remote Code Execution risks
    try:
        return str(ast.literal_eval(user_input))
    except (ValueError, SyntaxError):
        return "Invalid expression", 400