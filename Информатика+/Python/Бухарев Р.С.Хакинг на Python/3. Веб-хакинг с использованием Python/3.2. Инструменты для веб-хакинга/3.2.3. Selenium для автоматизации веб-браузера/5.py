from selenium import webdriver
import time

def check_email(url, username, password):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get(url)

    # Входим в почтовый ящик
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[text()='Login']").click()  # Замените по необходимости

    time.sleep(5)  # Ждем загрузки почтового ящика

    # Проверяем наличие новых сообщений
    new_messages = driver.find_elements("css selector", ".new-message")  # Замените селектор по необходимости
    for message in new_messages:
        print("Новое сообщение:", message.text)

    driver.quit()

# Пример использования
check_email("https://example-email.com", "your_email@example.com", "your_password")
