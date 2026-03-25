list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = []
for a, b in zip(list1, list2):
    sum_list.append(a + b)
print("Список суммы элементов:", sum_list)
