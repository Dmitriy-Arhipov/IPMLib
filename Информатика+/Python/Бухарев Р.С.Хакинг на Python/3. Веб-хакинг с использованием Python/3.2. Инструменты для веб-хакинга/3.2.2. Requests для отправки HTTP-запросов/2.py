import requests

def post_credentials(api_url, username, password):
    payload = {
        'username': username,
        'password': password
    }
    response = requests.post(api_url, data=payload)
    print("Ответ от сервера:")
    print(response.json())  # Выводим ответ в формате JSON

# Пример использования
post_credentials('https://example.com/api/login', 'your_username', 'your_password')
