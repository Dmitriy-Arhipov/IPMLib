num = int(input("Введите число: "))
sum_digits = sum(int(digit) for digit in str(num))
print(f"Сумма цифр числа {num} = {sum_digits}")
