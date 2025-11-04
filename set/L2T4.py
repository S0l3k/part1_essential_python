# Создайте множество всех студентов класса: {"Anna", "Bob", "Charlie", "Diana"}
# Создайте множество студентов, сдавших экзамен: {"Anna", "Charlie", "Diana"}
# Проверьте, все ли студенты сдали экзамен

set_all_students = {"Anna", "Bob", "Charlie", "Diana"}
set_students_passed_exam = {"Anna", "Charlie", "Diana"}
students_failed_exam = set_all_students ^ set_students_passed_exam

if len(set_all_students) == len(set_students_passed_exam):
    print('Все студенты сдали экзамен!')
else:
    print('К сожалению, не все студенты сдали экзамен - ', students_failed_exam)