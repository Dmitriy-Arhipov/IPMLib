import smtplib
from email.mime.text import MIMEText

def send_email(receiver, subject, content):
    sender = "your_email@gmail.com"
    password = "your_password"

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

receiver_email = input("Введите email получателя: ")
subject = input("Введите тему письма: ")
content = input("Введите текст письма: ")

send_email(receiver_email, subject, content)
print("Письмо успешно отправлено.")
