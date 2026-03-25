import requests
from bs4 import BeautifulSoup

def parse_web_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for title in soup.find_all('h1'):
            print(f"Title: {title.get_text()}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

url = "https://www.example.com"
parse_web_page(url)
