import random

number = 0
game_active = False

def start_game():
    global number, game_active
    number = random.randint(1, 100)
    game_active = True
    print("Игра началась! Угадайте число от 1 до 100.")

def guess_number():
    if not game_active:
        print("Сначала начните игру.")
        return
    guess = int(input("Введите число: "))
    if guess < number:
        print("Загаданное число больше.")
    elif guess > number:
        print("Загаданное число меньше.")
    else:
        print("Поздравляю! Вы угадали число!")
        global game_active
        game_active = False

def hint():
    if game_active:
        print(f"Загаданное число: {number}")
    else:
        print("Подсказка доступна только во время игры.")

commands = {
    "начать игру": start_game,
    "ввести число": guess_number,
    "показать подсказку": hint,
    "выход": lambda: print("Выход из игры")
}

while True:
    user_input = input("Введите команду (начать игру, ввести число, показать подсказку, выход): ").lower()
    if user_input == "выход":
        break
    elif user_input in commands:
        commands[user_input]()
    else:
        print("Неизвестная команда")
