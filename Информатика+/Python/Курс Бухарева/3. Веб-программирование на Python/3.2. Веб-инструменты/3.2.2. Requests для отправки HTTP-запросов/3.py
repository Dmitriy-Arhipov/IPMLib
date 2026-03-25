import requests

def check_websites_availability(urls):
    for url in urls:
        try:
            response = requests.get(url)
            print(f"{url}: {response.status_code} {response.reason}")
        except requests.exceptions.RequestException as e:
            print(f"{url}: Ошибка - {e}")

# Пример использования
check_websites_availability(['https://www.google.com', 'https://www.example.com', 'https://nonexistentwebsite.com'])
