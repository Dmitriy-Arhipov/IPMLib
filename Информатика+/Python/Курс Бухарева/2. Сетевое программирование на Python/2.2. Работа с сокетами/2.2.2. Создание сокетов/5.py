import smtplib

sender_email = input("Введите ваш email: ")
password = input("Введите пароль: ")
receiver_email = input("Введите email получателя: ")
subject = input("Введите тему письма: ")
message = input("Введите текст письма: ")

full_message = f"Subject: {subject}\n\n{message}"

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Устанавливаем защищённое соединение
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, full_message)
    print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    server.quit()
