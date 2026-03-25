import smtplib
from email.mime.text import MIMEText

def send_email(smtp_server, smtp_port, sender_email, receiver_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Включаем TLS
        server.login(sender_email, 'your_password')  # Вводим пароль
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email отправлен успешно!")

# Пример использования
send_email(
    smtp_server='smtp.example.com',
    smtp_port=587,
    sender_email='your_email@example.com',
    receiver_email='receiver_email@example.com',
    subject='Тестовое сообщение',
    body='Это тестовое сообщение, отправленное через SMTP.'
)
