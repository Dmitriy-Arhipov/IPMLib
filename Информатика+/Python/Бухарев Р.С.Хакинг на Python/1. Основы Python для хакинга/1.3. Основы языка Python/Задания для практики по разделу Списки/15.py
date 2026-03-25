numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
even_index_elements = numbers[::2]
print(f"Элементы на четных индексах: {even_index_elements}")
