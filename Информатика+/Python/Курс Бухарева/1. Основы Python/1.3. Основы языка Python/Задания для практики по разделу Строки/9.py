string = input("Введите строку: ")
doubled_string = ''.join([char * 2 for char in string])
print(f"Строка с удвоенными символами: {doubled_string}")
