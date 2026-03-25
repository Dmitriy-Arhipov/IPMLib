file_name = "user_input.txt"
num_lines = int(input("Сколько строк вы хотите ввести? "))

# Запись строк в файл
with open(file_name, 'w') as file:
    for _ in range(num_lines):
        line = input("Введите строку: ")
        file.write(line + "\n")

# Замена слов
search_word = input("Введите слово для поиска: ")
replace_word = input("Введите слово для замены: ")
new_file_name = "replaced_" + file_name

with open(file_name, 'r') as file, open(new_file_name, 'w') as new_file:
    for line in file:
        new_file.write(line.replace(search_word, replace_word))

print(f"Замена завершена. Результат сохранён в {new_file_name}.")
