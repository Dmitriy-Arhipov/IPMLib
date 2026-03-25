import smtplib
import socket

def send_email(receiver, subject, content):
    sender_email = "your_email@gmail.com"
    password = "your_password"
    message = f"Subject: {subject}\n\n{content}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver, message)
    server.quit()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Сервер запущен и готов принимать запросы...")

while True:
    client_socket, _ = server_socket.accept()
    receiver = client_socket.recv(1024).decode()
    subject = client_socket.recv(1024).decode()
    content = client_socket.recv(1024).decode()

    send_email(receiver, subject, content)
    client_socket.send("Письмо отправлено!".encode())
    client_socket.close()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

receiver = input("Введите email получателя: ")
subject = input("Введите тему письма: ")
content = input("Введите текст письма: ")

client_socket.send(receiver.encode())
client_socket.send(subject.encode())
client_socket.send(content.encode())

print(client_socket.recv(1024).decode())
client_socket.close()
