total = 0
count = 0
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    total += num
    count += 1
if count > 0:
    print("Среднее значение:", total / count)
else:
    print("Числа не были введены.")
