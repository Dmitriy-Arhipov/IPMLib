import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Сервер запущен, ожидаем подключения...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключение от {client_address}")
    client_socket.sendall(b"Добро пожаловать на сервер!")
    client_socket.close()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = client_socket.recv(1024)
print("Сообщение от сервера:", message.decode())
client_socket.close()
