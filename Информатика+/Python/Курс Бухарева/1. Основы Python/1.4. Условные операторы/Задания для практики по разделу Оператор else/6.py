correct_password = "mypassword"
password = input("Введите пароль: ")
if password == correct_password:
    print("Аутентификация прошла успешно.")
else:
    print("Неверный пароль.")
