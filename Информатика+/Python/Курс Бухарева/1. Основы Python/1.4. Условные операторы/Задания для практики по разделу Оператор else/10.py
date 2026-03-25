stock = int(input("Введите количество товара на складе: "))
threshold = 50
if stock < threshold:
    print("Необходимо пополнить запасы.")
else:
    print("Запасов достаточно.")
