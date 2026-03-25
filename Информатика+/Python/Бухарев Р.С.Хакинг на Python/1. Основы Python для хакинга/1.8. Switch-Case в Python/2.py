def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator in operations:
    result = operations[operator](num1, num2)
    print(f"Результат: {result}")
else:
    print("Неизвестный оператор")
