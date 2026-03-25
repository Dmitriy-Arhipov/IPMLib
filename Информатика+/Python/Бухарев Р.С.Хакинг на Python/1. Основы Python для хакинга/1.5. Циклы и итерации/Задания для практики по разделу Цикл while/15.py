while True:
    try:
        number = int(input("Введите целое число: "))
        print(f"Вы ввели число {number}.")
        break
    except ValueError:
        print("Некорректный ввод. Попробуйте снова.")
