file_name = input("Введите имя файла: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    print(f"Количество строк: {num_lines}")
    print(f"Количество слов: {num_words}")
    print(f"Количество символов: {num_chars}")
except FileNotFoundError:
    print("Файл не найден.")
