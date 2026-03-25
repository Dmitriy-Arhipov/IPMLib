numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
element = int(input("Введите элемент для поиска: "))
print(f"Элемент найден: {element in numbers}")
