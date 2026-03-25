weight = float(input("Введите ваш вес (в кг): "))
height = float(input("Введите ваш рост (в метрах): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Недостаточный вес.")
elif 18.5 <= bmi < 24.9:
    print("Нормальный вес.")
else:
    print("Избыточный вес.")
