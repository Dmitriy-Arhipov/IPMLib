text = input("Введите строку: ")
i = len(text) - 1
while i >= 0:
    print(text[i], end='')
    i -= 1
print()  # Для переноса строки
