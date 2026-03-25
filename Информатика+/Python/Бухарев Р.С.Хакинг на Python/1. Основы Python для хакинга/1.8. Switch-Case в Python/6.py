def greet_english():
    print("Hello!")

def greet_russian():
    print("Привет!")

def greet_spanish():
    print("¡Hola!")

greetings = {
    "английский": greet_english,
    "русский": greet_russian,
    "испанский": greet_spanish
}

language = input("Выберите язык (английский, русский, испанский): ").lower()
if language in greetings:
    greetings[language]()
else:
    print("Неизвестный язык")
