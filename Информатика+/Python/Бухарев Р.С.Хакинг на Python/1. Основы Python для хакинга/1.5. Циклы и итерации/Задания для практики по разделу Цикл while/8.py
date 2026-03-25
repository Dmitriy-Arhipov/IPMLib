max_num = None
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    if max_num is None or num > max_num:
        max_num = num
print("Наибольшее число:", max_num)
