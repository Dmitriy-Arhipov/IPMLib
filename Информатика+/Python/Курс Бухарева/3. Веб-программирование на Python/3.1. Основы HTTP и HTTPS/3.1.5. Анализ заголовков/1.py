import requests

def fetch_and_display_headers(urls):
    for url in urls:
        try:
            response = requests.get(url)
            print(f"URL: {url}\nHeaders:\n{response.headers}\n")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")

urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.nonexistentwebsite.com"
]

fetch_and_display_headers(urls)
