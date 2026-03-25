students_grades = {'Алексей': 85, 'Мария': 90, 'Иван': 78}
student_name = input("Введите имя студента для удаления: ")
students_grades.pop(student_name, None)
print(f"Обновлённый словарь: {students_grades}")
