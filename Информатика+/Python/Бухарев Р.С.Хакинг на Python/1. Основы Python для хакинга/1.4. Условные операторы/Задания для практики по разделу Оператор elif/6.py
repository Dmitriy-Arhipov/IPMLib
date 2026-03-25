age = int(input("Введите ваш возраст: "))
if age < 5:
    print("Билет бесплатный.")
elif 5 <= age <= 12:
    print("Детский билет.")
elif 13 <= age <= 59:
    print("Взрослый билет.")
else:
    print("Льготный билет.")
