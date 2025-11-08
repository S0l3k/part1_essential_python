# Дан список кортежей: [("math", 5), ("physics", 4), ("math", 4), ("history", 5), ("physics", 3)]
# Создайте словарь, где ключи - названия предметов, а значения - множества уникальных оценок
# Результат: {"math": {5, 4}, "physics": {4, 3}, "history": {5}}

input_tuple = [("math", 5), ("physics", 4), ("math", 4), ("history", 5), ("physics", 3)]

dict_with_subject_and_unique_grade = {}

for subject, grade in input_tuple:
    if subject not in dict_with_subject_and_unique_grade:
        dict_with_subject_and_unique_grade[subject] = set()
    dict_with_subject_and_unique_grade[subject].add(grade)

print(dict_with_subject_and_unique_grade)