num = int(input("Введите число: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} не является простым числом")
            break
    else:
        print(f"{num} является простым числом")
else:
    print(f"{num} не является простым числом")
