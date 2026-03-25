import socket

def handle_request(client_socket):
    request = client_socket.recv(1024).decode()
    if 'GET' in request:
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        response += "<html><body><h1>Привет, мир!</h1></body></html>"
        client_socket.sendall(response.encode())
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
print("HTTP-сервер запущен на порту 8080...")

while True:
    client_socket, _ = server_socket.accept()
    handle_request(client_socket)


import requests

response = requests.get('http://localhost:8080')
print(response.text)
