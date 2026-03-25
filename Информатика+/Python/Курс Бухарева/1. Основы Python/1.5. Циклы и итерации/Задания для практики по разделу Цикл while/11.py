password = ""
length = 8
while len(password) < length:
    char = input("Введите символ: ")
    password += char
print("Ваш пароль:", password)
