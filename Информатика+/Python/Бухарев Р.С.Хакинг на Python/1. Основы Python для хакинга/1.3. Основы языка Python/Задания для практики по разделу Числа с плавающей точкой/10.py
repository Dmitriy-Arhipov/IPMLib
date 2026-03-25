import math

radius = float(input("Введите радиус основания цилиндра: "))
height = float(input("Введите высоту цилиндра: "))

volume = math.pi * radius ** 2 * height
print(f"Объем цилиндра: {volume}")
