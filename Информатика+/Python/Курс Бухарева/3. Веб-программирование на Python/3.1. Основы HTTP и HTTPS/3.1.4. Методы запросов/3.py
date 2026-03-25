import requests

def test_vulnerabilities(urls):
    test_payloads = ["<script>alert('XSS')</script>", "' OR '1'='1";]
    
    for url in urls:
        for payload in test_payloads:
            try:
                response = requests.get(url + "?param=" + payload)
                if "error" in response.text.lower():  # Замените на нужное условие проверки
                    print(f"Potential vulnerability found at {url} with payload: {payload}")
            except requests.RequestException as e:
                print(f"Error testing {url}: {e}")

urls = [
    "https://www.example.com/search",
    "https://www.example.com/login"
]

test_vulnerabilities(urls)
