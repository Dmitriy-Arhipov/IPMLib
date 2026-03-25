import csv
from collections import defaultdict

file_name = "visits.csv"
monthly_visits = defaultdict(list)

try:
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            date, visits = row
            month = date[:7]  # Предполагается формат даты 'YYYY-MM-DD'
            monthly_visits[month].append(int(visits))

    print("Среднее количество посещений по месяцам:")
    for month, visits in monthly_visits.items():
        average_visits = sum(visits) / len(visits)
        print(f"{month}: {average_visits:.2f}")
except FileNotFoundError:
    print("CSV-файл не найден.")
