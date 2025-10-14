#На входе функция to_set() получает строку или список чисел. Преобразуйте их в множество. 
# На выходе должно получиться множество и его мощность.

def to_set(user_el):
    """Преобразует строку в множество и считает кол-во элементов в множестве(мощность)"""

    user_set = set(user_el)
    user_set_len = len(user_set)

    return print(user_set, user_set_len)

user_string = 'Любой текст подойдёт!'
user_numbers = [3, 1, 54, 12, 1, 2, 1, 1, 12, 13]

to_set(user_string)
to_set(user_numbers)