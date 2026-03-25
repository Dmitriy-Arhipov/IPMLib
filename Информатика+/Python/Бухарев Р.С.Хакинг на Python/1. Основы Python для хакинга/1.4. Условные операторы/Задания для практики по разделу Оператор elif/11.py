weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Недостаточный вес.")
elif 18.5 <= bmi < 24.9:
    print("Нормальный вес.")
elif 25 <= bmi < 29.9:
    print("Избыточный вес.")
else:
    print("Ожирение.")
