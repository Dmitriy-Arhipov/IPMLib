numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(f"Четные числа: {even_numbers}")
print(f"Нечетные числа: {odd_numbers}")
