def turn_on():
    print("Устройство включено")

def turn_off():
    print("Устройство выключено")

def standby():
    print("Устройство в режиме ожидания")

modes = {
    "включить": turn_on,
    "выключить": turn_off,
    "ожидание": standby
}

user_input = input("Введите режим (включить, выключить, ожидание): ").lower()
if user_input in modes:
    modes[user_input]()
else:
    print("Неизвестный режим")
