my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # Преобразование в список
my_list.append(4)         # Изменение списка
my_tuple = tuple(my_list)  # Преобразование обратно в кортеж
print(f"Измененный кортеж: {my_tuple}")
