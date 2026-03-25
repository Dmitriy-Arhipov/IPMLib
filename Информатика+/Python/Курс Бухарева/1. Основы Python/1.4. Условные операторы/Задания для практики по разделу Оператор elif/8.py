side1 = float(input("Введите длину первой стороны: "))
side2 = float(input("Введите длину второй стороны: "))
side3 = float(input("Введите длину третьей стороны: "))

if side1 == side2 == side3:
    print("Треугольник равносторонний.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Треугольник равнобедренный.")
else:
    print("Треугольник разносторонний.")
