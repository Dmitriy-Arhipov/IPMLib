import requests

def send_post_requests(url, data_list):
    for data in data_list:
        try:
            response = requests.post(url, json=data)
            print(f"Data: {data} - Response: {response.text}")
        except requests.RequestException as e:
            print(f"Error sending POST request: {e}")

url = "https://httpbin.org/post"  # Пример API
data_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

send_post_requests(url, data_list)
