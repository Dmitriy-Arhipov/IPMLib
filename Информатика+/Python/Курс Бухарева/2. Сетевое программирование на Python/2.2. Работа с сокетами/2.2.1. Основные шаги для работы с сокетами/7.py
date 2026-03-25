import socket

# Логика игры "Крестики-нолики"
# Реализуйте механизм ходов, проверки победы и взаимодействия между клиентами

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(2)
print("Сервер для игры 'Крестики-нолики' запущен...")

players = []
while len(players) < 2:
    client_socket, client_address = server_socket.accept()
    players.append(client_socket)
    print(f"Игрок {len(players)} подключился с адреса {client_address}")

# Далее можно управлять ходами, отправлять данные между игроками
# Пример обмена:
# player1.sendall("Ваш ход!".encode())
# message = player1.recv(1024).decode()
# player2.sendall(message.encode())


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Логика клиента для отправки и получения ходов в игре "Крестики-нолики"
while True:
    message = client_socket.recv(1024).decode()
    print(message)
    if "Ваш ход" in message:
        move = input("Введите ваш ход: ")
        client_socket.sendall(move.encode())

