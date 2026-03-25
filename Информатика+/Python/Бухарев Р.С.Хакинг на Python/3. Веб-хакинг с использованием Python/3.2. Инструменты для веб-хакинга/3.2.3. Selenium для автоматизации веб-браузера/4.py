from selenium import webdriver
import csv
import time

def scrape_shop(url):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get(url)

    # Ждем загрузки страницы
    time.sleep(2)

    products = []

    # Переходим к категориям
    category_links = driver.find_elements("css selector", ".category-link")  # Замените селектор по необходимости
    for category in category_links:
        category.click()
        time.sleep(2)

        # Собираем информацию о товарах
        product_elements = driver.find_elements("css selector", ".product")  # Замените селектор по необходимости
        for product in product_elements:
            name = product.find_element("css selector", ".product-name").text  # Замените селектор
            price = product.find_element("css selector", ".product-price").text  # Замените селектор
            products.append({"name": name, "price": price})

        driver.back()  # Возвращаемся к категориям
        time.sleep(2)

    # Сохраняем данные в CSV
    with open('products.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

    driver.quit()

# Пример использования
scrape_shop("https://example-shop.com")
