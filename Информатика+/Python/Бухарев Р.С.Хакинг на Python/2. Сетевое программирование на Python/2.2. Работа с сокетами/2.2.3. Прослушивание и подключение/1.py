import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 12345
BUFFER_SIZE = 1024
SAVE_DIR = 'uploads'

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def save_file(client_socket, filename):
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, 'wb') as file:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            file.write(data)
    print(f"Файл {filename} сохранен.")
    client_socket.send("Файл получен".encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print("Сервер готов принимать файлы...")

while True:
    client_socket, client_address = server_socket.accept()
    filename = client_socket.recv(BUFFER_SIZE).decode()
    save_file(client_socket, filename)
    client_socket.close()


import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

filename = input("Введите путь к файлу для отправки: ")

if os.path.isfile(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    client_socket.send(os.path.basename(filename).encode())

    with open(filename, 'rb') as file:
        while chunk := file.read(BUFFER_SIZE):
            client_socket.send(chunk)

    print(client_socket.recv(BUFFER_SIZE).decode())
    client_socket.close()
else:
    print("Файл не найден.")
