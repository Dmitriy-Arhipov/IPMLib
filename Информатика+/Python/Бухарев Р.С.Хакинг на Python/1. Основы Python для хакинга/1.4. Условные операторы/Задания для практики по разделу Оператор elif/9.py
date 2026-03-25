drink_number = int(input("Выберите номер напитка (1-5): "))
drinks = {1: "Вода", 2: "Чай", 3: "Кофе", 4: "Сок", 5: "Молоко"}
if drink_number in drinks:
    print(f"Вы выбрали: {drinks[drink_number]}")
else:
    print("Некорректный выбор.")
