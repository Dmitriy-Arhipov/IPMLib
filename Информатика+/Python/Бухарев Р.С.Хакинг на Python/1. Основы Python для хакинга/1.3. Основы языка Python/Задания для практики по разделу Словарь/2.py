students_grades = {'Алексей': 85, 'Мария': 90, 'Иван': 78}
student_name = input("Введите имя студента: ")
if student_name in students_grades:
    print(f"Оценка {student_name}: {students_grades[student_name]}")
else:
    print(f"Студент {student_name} не найден")
