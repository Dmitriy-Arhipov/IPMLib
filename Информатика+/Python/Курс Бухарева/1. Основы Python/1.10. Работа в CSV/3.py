import csv

file_name = "employees.csv"

num_employees = int(input("Сколько сотрудников вы хотите добавить? "))

with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Возраст", "Должность"])  # Заголовок
    for _ in range(num_employees):
        name = input("Введите имя сотрудника: ")
        age = input("Введите возраст сотрудника: ")
        position = input("Введите должность сотрудника: ")
        writer.writerow([name, age, position])

print("Информация о сотрудниках сохранена в файл.")
