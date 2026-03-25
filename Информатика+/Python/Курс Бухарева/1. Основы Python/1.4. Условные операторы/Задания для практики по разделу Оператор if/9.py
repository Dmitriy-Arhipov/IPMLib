month = int(input("Введите номер месяца (1-12): "))
if month in [12, 1, 2]:
    print("Зима.")
elif month in [3, 4, 5]:
    print("Весна.")
elif month in [6, 7, 8]:
    print("Лето.")
else:
    print("Осень.")
