n = int(input("Введите количество чисел: "))
numbers = [float(input(f"Введите число {i+1}: ")) for i in range(n)]
total_sum = sum(numbers)
print(f"Сумма введённых чисел: {total_sum}")
