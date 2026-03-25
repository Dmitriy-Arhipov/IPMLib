import math

num = float(input("Введите число: "))
if num >= 0:
    sqrt_num = math.sqrt(num)
    print(f"Квадратный корень из {num}: {sqrt_num}")
else:
    print("Невозможно вычислить квадратный корень из отрицательного числа")
