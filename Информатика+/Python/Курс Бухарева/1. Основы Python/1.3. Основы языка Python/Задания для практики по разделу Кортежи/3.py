my_tuple = (1, 2, 3)
# Попытка изменения элемента кортежа вызовет ошибку TypeError
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"Ошибка: {e}")
