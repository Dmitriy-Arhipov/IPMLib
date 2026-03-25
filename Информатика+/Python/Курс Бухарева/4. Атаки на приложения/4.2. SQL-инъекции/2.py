import requests
from urllib.parse import urlparse, parse_qs

def analyze_urls(url):
    response = requests.get(url)
    # Предположим, что мы ищем ссылки на странице
    links = []  # Сюда будем собирать все найденные ссылки
    if response.status_code == 200:
        # Найдите все ссылки (это упрощенная версия)
        for line in response.text.splitlines():
            if 'href' in line:
                start = line.find('http')
                end = line.find('"', start)
                if start != -1 and end != -1:
                    links.append(line[start:end])
    for link in links:
        parsed_url = urlparse(link)
        query_params = parse_qs(parsed_url.query)
        for param in query_params:
            print(f"Found parameter: {param} in URL: {link}")

if __name__ == "__main__":
    target_url = input("Enter the URL to analyze: ")
    analyze_urls(target_url)
