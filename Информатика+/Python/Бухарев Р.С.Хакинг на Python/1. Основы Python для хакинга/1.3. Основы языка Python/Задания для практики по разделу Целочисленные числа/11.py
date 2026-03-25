num = int(input("Введите число: "))
if str(num) == str(num)[::-1]:
    print(f"{num} является палиндромом")
else:
    print(f"{num} не является палиндромом")
