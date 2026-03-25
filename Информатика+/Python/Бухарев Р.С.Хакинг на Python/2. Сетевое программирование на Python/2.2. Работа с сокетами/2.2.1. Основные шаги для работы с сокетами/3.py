import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Сервер ожидает числа...")

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024).decode()
    numbers = list(map(int, data.split()))
    result = sum(numbers)
    print(f"Получены числа от {client_address}: {numbers}")
    client_socket.sendall(str(result).encode())
    client_socket.close()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
client_socket.sendall(f"{num1} {num2}".encode())

result = client_socket.recv(1024).decode()
print("Сумма:", result)
client_socket.close()
