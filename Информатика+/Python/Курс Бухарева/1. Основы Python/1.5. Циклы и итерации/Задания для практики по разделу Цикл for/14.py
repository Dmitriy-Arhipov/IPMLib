number = int(input("Введите число: "))
is_prime = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} — простое число.")
else:
    print(f"{number} — не является простым числом.")
