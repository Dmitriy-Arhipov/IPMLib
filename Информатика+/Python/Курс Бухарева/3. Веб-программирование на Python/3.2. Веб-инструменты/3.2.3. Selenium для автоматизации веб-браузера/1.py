from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def google_search(query):
    # Указываем путь к вашему веб-драйверу
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get("https://www.google.com")

    # Находим поле поиска
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)  # Нажимаем Enter

    # Ждем загрузки результатов
    time.sleep(2)

    # Выводим заголовки результатов
    results = driver.find_elements("css selector", "h3")
    for result in results:
        print(result.text)

    driver.quit()

# Пример использования
google_search("Python programming")
