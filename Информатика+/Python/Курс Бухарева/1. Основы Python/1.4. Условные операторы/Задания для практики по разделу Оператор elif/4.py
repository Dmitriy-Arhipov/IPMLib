score = int(input("Введите количество баллов (0-100): "))
if 90 <= score <= 100:
    print("Оценка: A")
elif 80 <= score < 90:
    print("Оценка: B")
elif 70 <= score < 80:
    print("Оценка: C")
elif 60 <= score < 70:
    print("Оценка: D")
else:
    print("Оценка: F")
