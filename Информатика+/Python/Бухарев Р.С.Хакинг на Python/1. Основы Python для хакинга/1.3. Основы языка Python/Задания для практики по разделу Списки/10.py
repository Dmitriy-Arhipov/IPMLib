numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
order = input("Введите 'возрастание' для сортировки по возрастанию или 'убывание' для сортировки по убыванию: ")

if order == 'возрастание':
    sorted_list = sorted(numbers)
elif order == 'убывание':
    sorted_list = sorted(numbers, reverse=True)
else:
    print("Некорректный ввод")

print(f"Отсортированный список: {sorted_list}")
