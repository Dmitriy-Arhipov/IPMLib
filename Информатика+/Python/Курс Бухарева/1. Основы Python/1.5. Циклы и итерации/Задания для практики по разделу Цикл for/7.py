strings = ['cat', 'dog', 'bird']
search = 'dog'
if search in strings:
    print(f"Строка '{search}' найдена на индексе {strings.index(search)}.")
else:
    print(f"Строка '{search}' не найдена.")
