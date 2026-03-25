import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 12345
BUFFER_SIZE = 4096
SAVE_DIR = 'server_files'

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def save_file(filename, client_socket):
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, 'wb') as f:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
    print(f"Файл {filename} успешно сохранен.")
    client_socket.send(f"Файл {filename} успешно получен".encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print("Сервер готов принимать файлы...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент: {client_address}")
    filename = client_socket.recv(BUFFER_SIZE).decode()
    save_file(filename, client_socket)
    client_socket.close()


import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 12345
BUFFER_SIZE = 4096

filename = input("Введите путь к файлу для отправки: ")

if os.path.isfile(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    client_socket.send(os.path.basename(filename).encode())

    with open(filename, 'rb') as f:
        while chunk := f.read(BUFFER_SIZE):
            client_socket.send(chunk)

    confirmation = client_socket.recv(BUFFER_SIZE).decode()
    print(confirmation)

    client_socket.close()
else:
    print("Файл не найден.")
