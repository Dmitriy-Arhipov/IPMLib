n = int(input("Введите число: "))
is_prime = True
i = 2
while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1
if is_prime and n > 1:
    print(f"{n} — простое число.")
else:
    print(f"{n} — не является простым числом.")
