import csv
from collections import defaultdict

file_name = "sales.csv"
monthly_revenue = defaultdict(float)

try:
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            date, revenue = row
            month = date[:7]  # Предположим, что дата в формате 'YYYY-MM-DD'
            monthly_revenue[month] += float(revenue)

    print("Выручка по месяцам:")
    for month, total in monthly_revenue.items():
        print(f"{month}: {total:.2f}")
except FileNotFoundError:
    print("CSV-файл не найден.")
