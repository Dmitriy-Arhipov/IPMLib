def command_one():
    print("Команда 1 выполнена")

def command_two():
    print("Команда 2 выполнена")

def command_three():
    print("Команда 3 выполнена")

commands = {
    "команда 1": command_one,
    "команда 2": command_two,
    "команда 3": command_three
}

user_input = input("Введите команду: ").lower()
if user_input in commands:
    commands[user_input]()
else:
    print("Неизвестная команда")
