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

START_INDEX = 0
END_INDEX = -1

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

    first_meet = None
    second_meet = None

    if rnd_el in tpl:
        first_meet = tpl.index(rnd_el)
    if tpl.count(rnd_el) > 1:
        second_meet = tpl.index(rnd_el, first_meet + 1) + 1
    else:
        second_meet = END_INDEX
    
    return tpl[first_meet:second_meet]

print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))