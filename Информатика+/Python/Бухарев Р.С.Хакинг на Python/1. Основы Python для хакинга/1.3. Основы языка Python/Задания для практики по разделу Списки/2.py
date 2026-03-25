from functools import reduce

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
product = reduce(lambda x, y: x * y, numbers)
print(f"Произведение чисел: {product}")
