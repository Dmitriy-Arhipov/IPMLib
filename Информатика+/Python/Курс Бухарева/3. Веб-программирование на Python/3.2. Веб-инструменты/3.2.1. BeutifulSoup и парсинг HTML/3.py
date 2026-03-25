import requests
from bs4 import BeautifulSoup

def extract_table_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Предположим, что таблица имеет тег <table>
    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        data = [col.text.strip() for col in cols]
        print(data)

# Пример использования
extract_table_data('https://example-website-with-table.com')
