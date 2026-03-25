def handle_zero_division():
    print("Ошибка: деление на ноль.")

def handle_value_error():
    print("Ошибка: введено не число.")

error_handlers = {
    "zero_division": handle_zero_division,
    "value_error": handle_value_error
}

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
    print(f"Результат: {result}")
except ZeroDivisionError:
    error_handlers["zero_division"]()
except ValueError:
    error_handlers["value_error"]()
