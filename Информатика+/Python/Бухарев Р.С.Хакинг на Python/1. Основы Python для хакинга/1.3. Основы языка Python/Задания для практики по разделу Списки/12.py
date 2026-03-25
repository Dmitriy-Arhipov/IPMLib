list1 = list(map(int, input("Введите первый отсортированный список: ").split()))
list2 = list(map(int, input("Введите второй отсортированный список: ").split()))

merged_list = sorted(list1 + list2)
print(f"Объединенный отсортированный список: {merged_list}")
