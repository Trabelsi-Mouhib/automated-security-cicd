import sqlite3

# VULNERABILITY 1: Hardcoded AWS Secret Key (Secret Leak)
# Security tools look for standard API key formats like this.
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
DATABASE_PASSWORD = "SuperSecretPassword123!"

def get_user_data(username):
    # VULNERABILITY 2: SQL Injection (Insecure Code Logic)
    # Concatenating raw input into a SQL query allows attackers to alter database logic.
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def run_calculator(user_input):
    # VULNERABILITY 3: Unsafe Eval (Remote Code Execution)
    # Never use eval() on untrusted user input.
    return eval(user_input)

if __name__ == "__main__":
    print("Application started...")
