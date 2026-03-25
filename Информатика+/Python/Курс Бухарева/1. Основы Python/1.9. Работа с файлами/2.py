file_name = "numbers.txt"

# Запись чисел в файл
with open(file_name, 'w') as file:
    for number in range(1, 11):
        file.write(f"{number}\n")

# Чтение чисел и вычисление суммы
total = 0
with open(file_name, 'r') as file:
    for line in file:
        total += int(line.strip())

print(f"Сумма чисел: {total}")
