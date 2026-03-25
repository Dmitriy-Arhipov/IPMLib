import csv

file_name = "students.csv"

try:
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            name, age, average_score = row
            print(f"Имя: {name}, Возраст: {age}, Средний балл: {average_score}")
except FileNotFoundError:
    print("CSV-файл не найден.")
