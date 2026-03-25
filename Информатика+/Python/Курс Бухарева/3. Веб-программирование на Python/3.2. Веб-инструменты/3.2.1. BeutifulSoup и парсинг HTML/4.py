import requests
import csv
from bs4 import BeautifulSoup

def extract_data_and_save_to_csv(url, csv_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Предположим, что данные находятся в <div> с классом 'data-item'
    data_items = soup.find_all('div', class_='data-item')

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Value'])  # Заголовки столбцов
        for item in data_items:
            title = item.find('h3').text.strip()
            value = item.find('span', class_='value').text.strip()
            writer.writerow([title, value])

# Пример использования
extract_data_and_save_to_csv('https://example-data-website.com', 'data.csv')
