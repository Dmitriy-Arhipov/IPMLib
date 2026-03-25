numbers = [float(input(f"Введите число {i+1}: ")) for i in range(5)]
average = sum(numbers) / len(numbers)
print(f"Среднее арифметическое: {average}")
