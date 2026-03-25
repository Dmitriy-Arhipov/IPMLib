numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
n = int(input("Введите количество позиций для сдвига: "))
shifted_list = numbers[-n:] + numbers[:-n]
print(f"Список после сдвига: {shifted_list}")
