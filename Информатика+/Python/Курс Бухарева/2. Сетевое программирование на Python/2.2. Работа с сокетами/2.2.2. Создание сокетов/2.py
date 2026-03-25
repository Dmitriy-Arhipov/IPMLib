import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Сервер готов к приему файлов...")

while True:
    client_socket, client_address = server_socket.accept()
    with open("received_file.txt", 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
    print("Файл успешно сохранен.")
    client_socket.close()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

with open("file_to_send.txt", 'rb') as file:
    data = file.read(1024)
    while data:
        client_socket.send(data)
        data = file.read(1024)

print("Файл успешно отправлен.")
client_socket.close()
