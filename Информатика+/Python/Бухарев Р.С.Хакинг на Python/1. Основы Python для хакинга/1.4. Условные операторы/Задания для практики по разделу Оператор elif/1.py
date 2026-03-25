hour = int(input("Введите текущий час (0-23): "))
if 5 <= hour <= 11:
    print("Утро.")
elif 12 <= hour <= 17:
    print("День.")
elif 18 <= hour <= 22:
    print("Вечер.")
else:
    print("Ночь.")
