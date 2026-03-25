import requests
from bs4 import BeautifulSoup

def extract_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Предположим, что заголовки находятся в теге <h2> с классом 'headline'
    headlines = soup.find_all('h2', class_='headline')
    for headline in headlines:
        print(headline.text.strip())

# Пример использования
extract_news_headlines('https://example-news-website.com')
