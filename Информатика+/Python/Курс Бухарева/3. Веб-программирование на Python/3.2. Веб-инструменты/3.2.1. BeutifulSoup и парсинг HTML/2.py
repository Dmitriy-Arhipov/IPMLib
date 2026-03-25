import requests
from bs4 import BeautifulSoup

def extract_product_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Предположим, что цены находятся в теге <span> с классом 'price'
    products = soup.find_all('div', class_='product')
    for product in products:
        title = product.find('h3').text.strip()
        price = product.find('span', class_='price').text.strip()
        print(f'Product: {title}, Price: {price}')

# Пример использования
extract_product_prices('https://example-ecommerce-website.com')
