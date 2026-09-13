import sqlite3

# VULNERABILITY 1: Hardcoded AWS Credential Pattern (Secret Leak)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN78912345"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def get_user_data(username):
    # VULNERABILITY 2: SQL Injection (Insecure Code Logic)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def run_calculator(user_input):
    # VULNERABILITY 3: Unsafe Eval (Remote Code Execution)
    return eval(user_input)

if __name__ == "__main__":
    print("Application started...")