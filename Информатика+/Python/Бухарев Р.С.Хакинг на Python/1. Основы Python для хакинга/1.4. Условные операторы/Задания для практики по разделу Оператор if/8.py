correct_password = "secret123"
password = input("Введите пароль: ")
if password == correct_password:
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")
