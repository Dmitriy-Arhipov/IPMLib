numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
unique_numbers = list(set(numbers))
print(f"Список без дубликатов: {unique_numbers}")
