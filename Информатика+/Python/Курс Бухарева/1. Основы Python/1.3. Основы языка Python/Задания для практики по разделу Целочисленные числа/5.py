def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = int(input("Введите число: "))
print(f"Факториал {n} = {factorial(n)}")
