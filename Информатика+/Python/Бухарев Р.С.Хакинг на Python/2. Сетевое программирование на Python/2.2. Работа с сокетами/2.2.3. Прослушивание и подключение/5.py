import socket
import threading

board = [' ' for _ in range(9)]
players = []

def check_winner():
    win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def handle_game(player_socket, symbol):
    while True:
        move = int(player_socket.recv(1024).decode())
        if board[move] == ' ':
            board[move] = symbol
            winner = check_winner()
            for player in players:
                player.send(f"{symbol} сделал ход на позицию {move}".encode())
                player.send("".join(board).encode())
                if winner:
                    player.send(f"Победитель: {winner}".encode())
            if winner:
                break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(2)

for i in range(2):
    player_socket, _ = server_socket.accept()
    players.append(player_socket)
    symbol = 'X' if i == 0 else 'O'
    player_socket.send(f"Ваш символ: {symbol}".encode())
    threading.Thread(target=handle_game, args=(player_socket, symbol)).start()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

symbol = client_socket.recv(1024).decode()
print(symbol)

while True:
    move = input("Ваш ход (0-8): ")
    client_socket.send(move.encode())
    print(client_socket.recv(1024).decode())
    print("".join(client_socket.recv(1024).decode()))
