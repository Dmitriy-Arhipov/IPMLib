import requests

def security_analysis(urls):
    for url in urls:
        try:
            response = requests.get(url)
            headers = response.headers

            if "X-Frame-Options" not in headers:
                print(f"Warning: X-Frame-Options header missing in {url}")

            if "Strict-Transport-Security" not in headers:
                print(f"Warning: Strict-Transport-Security header missing in {url}")

            if "Content-Security-Policy" not in headers:
                print(f"Warning: Content-Security-Policy header missing in {url}")

        except requests.RequestException as e:
            print(f"Error analyzing security for {url}: {e}")

urls = [
    "https://www.example.com",
    "https://www.example.org"
]

security_analysis(urls)
