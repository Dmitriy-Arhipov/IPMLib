correct_password = "password123"
while True:
    password = input("Введите пароль: ")
    if password == correct_password:
        print("Пароль верный!")
        break
    else:
        print("Неправильный пароль. Попробуйте снова.")
