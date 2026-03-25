from selenium import webdriver
import time

def register_on_website(url, username, email, password):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get(url)

    # Заполняем форму регистрации
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "email").send_keys(email)
    driver.find_element("name", "password").send_keys(password)

    # Отправляем форму
    driver.find_element("xpath", "//button[text()='Register']").click()  # Измените по необходимости

    time.sleep(2)  # Ждем завершения регистрации
    driver.quit()

# Пример использования
register_on_website("https://example.com/register", "testuser", "test@example.com", "password123")
