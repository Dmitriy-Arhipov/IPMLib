age = int(input("Введите ваш возраст: "))
if 0 <= age <= 2:
    print("Младенец.")
elif 3 <= age <= 12:
    print("Ребенок.")
elif 13 <= age <= 19:
    print("Подросток.")
elif 20 <= age <= 64:
    print("Взрослый.")
else:
    print("Пожилой.")
