numbers = []
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    numbers.append(num)
print("Список введённых чисел:", numbers)
