lang_number = int(input("Выберите номер языка программирования (1-5): "))
languages = {1: "Python", 2: "Java", 3: "C++", 4: "JavaScript", 5: "Ruby"}
if lang_number in languages:
    print(f"Вы выбрали: {languages[lang_number]}")
else:
    print("Некорректный выбор.")
