import sqlite3

# VULNERABILITY 1: Hardcoded Private Key (Secret Leak)
# GitHub Push Protection allows dummy RSA key headers, but TruffleHog flags private key structures.
FAKE_RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Z1fX23456789abcdef0123456789abcdef0123456789abcd
ef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcd
ef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcd
ef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcd
IDAQABAoIBAQC0Z1fX23456789abcdef0123456789abcdef0123456789abcdef
-----END RSA PRIVATE KEY-----"""

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