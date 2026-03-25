tasks = []

def add_task():
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def remove_task():
    task = input("Введите задачу для удаления: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Задача '{task}' удалена.")
    else:
        print(f"Задача '{task}' не найдена.")

def show_tasks():
    if tasks:
        print("Список задач:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Список задач пуст.")

def update_task():
    show_tasks()
    idx = int(input("Введите номер задачи для изменения: ")) - 1
    if 0 <= idx < len(tasks):
        new_task = input("Введите новую задачу: ")
        tasks[idx] = new_task
        print(f"Задача обновлена: {new_task}")
    else:
        print("Неверный номер задачи.")

commands = {
    "добавить": add_task,
    "удалить": remove_task,
    "показать": show_tasks,
    "изменить": update_task
}

while True:
    user_input = input("Введите команду (добавить, удалить, показать, изменить, выход): ").lower()
    if user_input == "выход":
        break
    elif user_input in commands:
        commands[user_input]()
    else:
        print("Неизвестная команда")
