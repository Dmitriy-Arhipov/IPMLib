day = input("Введите день недели: ").lower()
working_days = ["понедельник", "вторник", "среда", "четверг", "пятница"]
if day in working_days:
    print(f"{day.capitalize()} — это рабочий день.")
else:
    print(f"{day.capitalize()} — это выходной.")
