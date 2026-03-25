number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
if number1 > number2:
    print(f"Наибольшее число: {number1}")
elif number1 < number2:
    print(f"Наибольшее число: {number2}")
else:
    print("Числа равны.")
