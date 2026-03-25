from selenium import webdriver
import time

def view_news(url):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get(url)

    # Ждем загрузки страницы
    time.sleep(2)

    # Находим все ссылки на новости
    news_links = driver.find_elements("css selector", "a.news-link")  # Замените селектор по необходимости

    for link in news_links:
        link.click()  # Переходим к новости
        time.sleep(2)

        # Выводим заголовок и краткое описание
        title = driver.find_element("css selector", "h1").text  # Измените селектор по необходимости
        description = driver.find_element("css selector", ".description").text  # Измените селектор по необходимости
        print(f"Заголовок: {title}\nОписание: {description}\n")

        driver.back()  # Возвращаемся на главную страницу новостей
        time.sleep(2)

    driver.quit()

# Пример использования
view_news("https://newswebsite.com")
