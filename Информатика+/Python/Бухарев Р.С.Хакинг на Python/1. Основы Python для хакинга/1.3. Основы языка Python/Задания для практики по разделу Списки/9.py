list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))
list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))
combined_list = list1 + list2
print(f"Объединенный список: {combined_list}")
