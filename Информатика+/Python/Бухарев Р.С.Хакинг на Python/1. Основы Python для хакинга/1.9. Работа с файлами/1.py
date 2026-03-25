file_name = "text.txt"
user_text = input("Введите текст для записи в файл: ")

# Сохранение текста в файл
with open(file_name, 'w') as file:
    file.write(user_text)

# Чтение содержимого файла и вывод на экран
with open(file_name, 'r') as file:
    content = file.read()

print("Содержимое файла:")
print(content)
