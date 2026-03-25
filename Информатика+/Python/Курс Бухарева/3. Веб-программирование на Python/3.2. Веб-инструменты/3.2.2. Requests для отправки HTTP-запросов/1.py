import requests

def get_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        print("Полученные данные:")
        print(response.json())  # Выводим данные в формате JSON
    else:
        print(f"Ошибка: {response.status_code}")

# Пример использования
get_data_from_api('https://jsonplaceholder.typicode.com/posts')
