num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num1 % num2 == 0:
    print(f"{num1} делится на {num2} без остатка.")
else:
    print(f"{num1} не делится на {num2} без остатка.")
