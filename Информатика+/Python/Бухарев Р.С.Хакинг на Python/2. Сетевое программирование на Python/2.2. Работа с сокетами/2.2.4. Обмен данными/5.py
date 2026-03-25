import socket
import threading

board_size = 5
players = []
boards = [[' ' * board_size] for _ in range(2)]  # Простая игровая доска

def handle_game(player_socket, player_id):
    opponent_id = 1 if player_id == 0 else 0
    while True:
        coords = player_socket.recv(1024).decode()
        x, y = map(int, coords.split(','))
        if boards[opponent_id][x][y] == ' ':
            result = "Мимо"
        else:
            result = "Попадание!"
        player_socket.send(result.encode())
        if result == "Попадание!":
            # Логика завершения игры
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(2)

for i in range(2):
    player_socket, _ = server_socket.accept()
    players.append(player_socket)
    threading.Thread(target=handle_game, args=(player_socket, i)).start()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    coords = input("Введите координаты выстрела (x, y): ")
    client_socket.send(coords.encode())
    result = client_socket.recv(1024).decode()
    print(result)
    if result == "Попадание!":
        break
