import requests
import time
from bs4 import BeautifulSoup

def monitor_changes(url, check_interval):
    previous_content = None

    while True:
        response = requests.get(url)
        current_content = response.text

        if previous_content and previous_content != current_content:
            print("Page has changed!")
            # Здесь можно добавить код для уведомления пользователя

        previous_content = current_content
        time.sleep(check_interval)

# Пример использования
monitor_changes('https://example-website-to-monitor.com', 60)  # Проверять каждые 60 секунд
