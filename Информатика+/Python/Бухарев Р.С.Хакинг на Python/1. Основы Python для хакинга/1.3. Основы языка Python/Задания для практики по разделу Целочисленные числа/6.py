import math

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Уравнение имеет два корня: {root1} и {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Уравнение имеет один корень: {root}")
else:
    print("Уравнение не имеет вещественных корней")
