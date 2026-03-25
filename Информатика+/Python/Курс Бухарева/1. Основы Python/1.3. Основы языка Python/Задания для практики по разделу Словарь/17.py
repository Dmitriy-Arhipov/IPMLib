students_grades = {'Алексей': 85, 'Мария': 90}
default_value = students_grades.setdefault('Иван', 75)
print(f"Значение для Ивана: {default_value}")
print(f"Обновлённый словарь: {students_grades}")
