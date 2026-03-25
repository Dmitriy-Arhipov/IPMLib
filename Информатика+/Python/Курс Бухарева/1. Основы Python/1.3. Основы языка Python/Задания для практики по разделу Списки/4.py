numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
average = sum(numbers) / len(numbers)
print(f"Среднее значение: {average}")
