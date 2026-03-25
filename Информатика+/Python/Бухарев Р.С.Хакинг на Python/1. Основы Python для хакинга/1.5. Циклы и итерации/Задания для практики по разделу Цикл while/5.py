n = int(input("Введите число: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print("Факториал:", factorial)
