import requests

def check_status_codes(urls):
    for url in urls:
        try:
            response = requests.get(url)
            print(f"URL: {url} - Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error with URL: {url} - {e}")

urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.nonexistentwebsite.com"
]

check_status_codes(urls)
