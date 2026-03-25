file_name = input("Введите имя файла: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
    print("Содержимое файла в обратном порядке:")
    for line in reversed(lines):
        print(line.strip())
except FileNotFoundError:
    print("Файл не найден.")
