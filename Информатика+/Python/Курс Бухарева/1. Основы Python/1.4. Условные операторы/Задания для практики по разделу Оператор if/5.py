temperature = float(input("Введите температуру: "))
if temperature < 0:
    print("Холодно.")
elif 0 <= temperature <= 20:
    print("Тепло.")
else:
    print("Жарко.")
