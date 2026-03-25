import requests

def analyze_http_headers(urls):
    forbidden_headers = ["X-Powered-By", "Server"]

    for url in urls:
        try:
            response = requests.get(url)
            headers = response.headers

            for header in forbidden_headers:
                if header in headers:
                    print(f"Forbidden header '{header}' found in {url}")

            # Проверка на аномальные значения
            if "Content-Security-Policy" not in headers:
                print(f"Warning: No Content-Security-Policy found in {url}")
            else:
                print(f"Valid CSP found in {url}")

        except requests.RequestException as e:
            print(f"Error analyzing {url}: {e}")

urls = [
    "https://www.example.com",
    "https://www.example.org"
]

analyze_http_headers(urls)
