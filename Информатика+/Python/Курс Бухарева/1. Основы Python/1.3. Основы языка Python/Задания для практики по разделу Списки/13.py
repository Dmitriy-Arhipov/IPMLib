numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
element = int(input("Введите элемент для подсчета: "))
count = numbers.count(element)
print(f"Элемент {element} встречается {count} раз(а)")
