import requests

def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Файл загружен: {local_filename}")
    else:
        print(f"Ошибка при загрузке файла: {response.status_code}")

# Пример использования
download_file('https://www.example.com/sample.pdf', 'downloaded_sample.pdf')
