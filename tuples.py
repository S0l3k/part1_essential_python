#Кортеж (tuple) - неизменяемый тип данных, который предназначен для хранения упорядоченной инф.

# single_elements_tuple = (42,)
# single_elements_tuple_copy = (42)

# print(type(single_elements_tuple))
# print(type(single_elements_tuple_copy))

# def tpl_sort(tpl):
#     """Сортирует кортеж из целых числе и возвращате его. Если в нем встречаются элементы не 
#     относящиеся к целым числам, то возвращате исходный кортеж"""

#     for i in tpl:
#         if not isinstance(i, int):
#             return tpl
#     return tuple(sorted(tpl))

# print(tpl_sort((5, 5, 3, 1, 9)))
# print(tpl_sort((5, 5, 2.1, '1', 9)))

# START_INDEX = 0
# END_INDEX = -1

def slicer(tpl, rnd_el):
    """Принимает кортеж и случайные элемент. Должен вернуть кортеж, начинающийся с первого 
    появления элемента в нём и заканчиающийся вторым появление элемента в нём включительно.
    Если элемента нет вовсе - вернуть пустой кортеж.
    Если элемент встрчается только один раз, то вернуть кортеж, который начинается с него и идёт
    до конца исходного"""

    # first_meet = None
    # second_meet = None
    
    # for i in tpl:
    #     if rnd_el not in tpl:
    #         return tuple()
    #     elif tpl.count(rnd_el) == 1:
    #         rnd_el_index = tpl.index(rnd_el)
    #         return tpl[rnd_el_index:]
    #     elif tpl.count(rnd_el) == 2:
    #         first_meet = tpl.index(rnd_el)
    #         second_meet = tpl.index(rnd_el, first_meet)
    #         return tuple[first_meet:second_meet]

    # first_meet = None
    # second_meet = None

    # if rnd_el in tpl:
    #     first_meet = tpl.index(rnd_el)
    # if tpl.count(rnd_el) > 1:
    #     second_meet = tpl.index(rnd_el, first_meet + 1) + 1
    # else:
    #     second_meet = END_INDEX
    
    # return tpl[first_meet:second_meet]

    if rnd_el not in tpl:
        return tuple()
    
    first_meet = tpl.index(rnd_el)

    if tpl.count(rnd_el) == 1:
        return tpl[first_meet:]
    else:
        second_meet = tpl.index(rnd_el, first_meet + 1)
        return tpl[first_meet:second_meet + 1]

print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

def sieve(lst) -> tuple:
    """Принимает список, должна сформировать кортеж с уникальными элементами и вернуть кортеж."""

    unique = []

    for item in reversed(lst):
        if item not in unique:
            unique.append(item)
    
    return tuple(unique)
    
    # reversed_list = reversed(list)
    # enter_list_to_set = set(reversed_list)
    # set_to_tuple = tuple(enter_list_to_set)

    # return set_to_tuple

print(sieve([1, 2, 3, 3, 2]))
print(sieve([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))
print(sieve((1, 2, 3, 4, 5, 6, 7)))