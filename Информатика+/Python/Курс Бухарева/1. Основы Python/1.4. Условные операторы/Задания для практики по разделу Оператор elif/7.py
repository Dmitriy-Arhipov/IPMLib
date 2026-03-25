number = int(input("Введите число: "))
if number > 0:
    print("Число положительное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число равно нулю.")

if number % 2 == 0:
    print("Число четное.")
else:
    print("Число нечетное.")
