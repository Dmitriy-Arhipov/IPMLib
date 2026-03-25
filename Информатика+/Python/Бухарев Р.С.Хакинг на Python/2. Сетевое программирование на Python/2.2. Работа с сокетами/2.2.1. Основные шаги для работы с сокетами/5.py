import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Сервер времени запущен...")

while True:
    client_socket, client_address = server_socket.accept()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_socket.sendall(current_time.encode())
    client_socket.close()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

current_time = client_socket.recv(1024).decode()
print("Текущее время:", current_time)
client_socket.close()
