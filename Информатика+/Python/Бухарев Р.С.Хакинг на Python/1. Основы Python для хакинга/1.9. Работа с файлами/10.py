import csv

file_name = input("Введите имя CSV-файла: ")
new_file_name = "updated_" + file_name

# Чтение данных из CSV, модификация и запись в новый файл
try:
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
    # Внесите изменения в rows по вашему усмотрению
    # Например, добавим "Обработано" в конец каждой строки
    for row in rows:
        row.append("Обработано")

    with open(new_file_name, 'w', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(rows)

    print(f"Изменения сохранены в {new_file_name}.")
except FileNotFoundError:
    print("CSV-файл не найден.")
