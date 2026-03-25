import csv
import os

output_file = "merged_data.csv"
input_files = ["data1.csv", "data2.csv", "data3.csv"]  # Добавьте свои файлы

with open(output_file, 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Имя", "Возраст", "Средний балл"])  # Заголовок

    for input_file in input_files:
        if os.path.exists(input_file):
            with open(input_file, 'r', newline='') as in_file:
                reader = csv.reader(in_file)
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    writer.writerow(row)
        else:
            print(f"Файл {input_file} не найден.")

print(f"Данные объединены и сохранены в {output_file}.")
