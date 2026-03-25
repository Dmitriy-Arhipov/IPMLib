import random
target = random.randint(1, 100)
guess = None

while guess != target:
    guess = int(input("Угадайте число от 1 до 100: "))
    if guess < target:
        print("Загаданное число больше.")
    elif guess > target:
        print("Загаданное число меньше.")
    else:
        print("Поздравляю, вы угадали!")
