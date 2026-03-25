import socket
import threading

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Сервер чата запущен...")

while True:
    client_socket, _ = server_socket.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

threading.Thread(target=receive_messages, args=(client_socket,)).start()

while True:
    message = input("Введите сообщение: ")
    client_socket.send(message.encode())
