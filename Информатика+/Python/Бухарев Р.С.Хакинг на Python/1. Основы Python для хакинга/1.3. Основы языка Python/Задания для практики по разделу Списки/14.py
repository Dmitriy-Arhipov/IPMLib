numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
element = int(input("Введите элемент для удаления: "))
if element in numbers:
    numbers.remove(element)
    print(f"Обновленный список: {numbers}")
else:
    print("Элемент не найден в списке")
