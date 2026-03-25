string = input("Введите строку: ")
old_char = input("Введите символ для замены: ")
new_char = input("Введите символ-замену: ")

if len(old_char) == 1 and len(new_char) == 1:
    modified_string = string.replace(old_char, new_char)
    print(f"Изменённая строка: {modified_string}")
else:
    print("Пожалуйста, введите только по одному символу для замены и замены.")
