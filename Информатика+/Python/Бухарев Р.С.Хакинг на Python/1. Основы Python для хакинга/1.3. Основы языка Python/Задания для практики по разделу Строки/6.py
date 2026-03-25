string = input("Введите строку: ")
start = int(input("Введите начальный индекс: "))
end = int(input("Введите конечный индекс: "))

if 0 <= start <= end < len(string):
    substring = string[start:end+1]
    print(f"Извлечённая подстрока: {substring}")
else:
    print("Некорректные индексы")
