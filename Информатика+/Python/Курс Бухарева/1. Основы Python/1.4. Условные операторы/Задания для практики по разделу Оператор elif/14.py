vehicle_number = int(input("Выберите номер транспортного средства (1-5): "))
vehicles = {1: "Велосипед", 2: "Мотоцикл", 3: "Автомобиль", 4: "Автобус", 5: "Поезд"}
if vehicle_number in vehicles:
    print(f"Вы выбрали: {vehicles[vehicle_number]}")
else:
    print("Некорректный выбор.")
