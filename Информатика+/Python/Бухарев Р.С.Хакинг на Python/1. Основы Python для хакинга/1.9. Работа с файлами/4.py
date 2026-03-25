source_file = input("Введите имя исходного файла: ")
destination_file = input("Введите имя файла для копирования: ")

try:
    with open(source_file, 'r') as src, open(destination_file, 'w') as dst:
        dst.write(src.read())
    print("Файл успешно скопирован.")
except FileNotFoundError:
    print("Исходный файл не найден.")
