file_name = input("Введите имя файла: ")
user_text = input("Введите текст для записи в файл: ")

try:
    with open(file_name, 'x') as file:  # Создание файла, если его не существует
        file.write(user_text)
except FileExistsError:
    action = input("Файл уже существует. Перезаписать (w) или добавить в конец (a)? ")
    mode = 'w' if action == 'w' else 'a'
    with open(file_name, mode) as file:
        file.write(user_text)

print("Операция завершена.")
