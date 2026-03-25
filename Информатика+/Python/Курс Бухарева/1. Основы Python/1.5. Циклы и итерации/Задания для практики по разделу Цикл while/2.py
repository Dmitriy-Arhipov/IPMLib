total = 0
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    total += num
print("Сумма всех введённых чисел:", total)
