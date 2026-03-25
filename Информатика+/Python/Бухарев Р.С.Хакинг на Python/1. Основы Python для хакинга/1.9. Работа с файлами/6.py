file_name = input("Введите имя файла: ")
search_word = input("Введите слово для поиска: ")
replace_word = input("Введите слово для замены: ")
new_file_name = "new_" + file_name

try:
    with open(file_name, 'r') as file, open(new_file_name, 'w') as new_file:
        for line in file:
            new_file.write(line.replace(search_word, replace_word))
    print(f"Замена завершена. Результат сохранён в {new_file_name}.")
except FileNotFoundError:
    print("Файл не найден.")
