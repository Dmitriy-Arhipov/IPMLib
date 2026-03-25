import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Эхо-сервер запущен...")

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)
    print(f"Получено от {client_address}: {data.decode()}")
    client_socket.sendall(data)
    client_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = input("Введите сообщение: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024).decode()
print("Ответ от сервера:", data)
client_socket.close()
