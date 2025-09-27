# empty_list = []
# print(type(empty_list))

# empty_list = list()
# print(type(empty_list))

some_list = ['колбаса', 'тыква', 'хлеб', 'молоко', 'яйца']
print(some_list)

# print(some_list[0])
# print(some_list[1])
# print(some_list[-1])

# some_list[2] = 'картофель'
# print(some_list)

# another_list = ['apple', 'eggs', 'milk', 'orange']
# combined_list = some_list + another_list
# print(combined_list)

# first, second, third, other, othertwo = some_list
# print(first, type(first))
# print(second)
# print(third)

# for item in some_list:
#     print(f'Товар в корзине: ', item)
# print(f'Кол-во товара в корзине: ', len(some_list))

# another_list = ['колбаса', 'тыква', 'хлеб', 'молоко', 'яйца']
# other_list = ['хлеб', 'молоко', 'яйца']

# if another_list == some_list:
#     print('Значения совпадают. Всё верно!')
# else:
#     print('Значения разные. Увы!')

# if other_list == some_list:
#     print('Значения совпадают. Всё верно!')
# else:
#     print('Значения разные. Увы!')

# print(max(some_list)) #выводит максимальное значение по идексу?
# print(min(some_list)) #выводит минимальное занчение по индексу?
# print(sorted(some_list, key=None, reverse=False)) #сортирует значения в алфавитном порядке

some_list.append('хлеб')
print(some_list)
some_list.insert(3, 'бублик')
print(some_list)

first_hlem_index = some_list.index('хлеб') #говорит какой индекс в списке у нужного элемента, если их несколько, то выводит первый совпавший
print(f'Элемент "хлеб" был добавлен на позицияю ', first_hlem_index )
print(some_list.index('хлеб'))

# some_list.remove('хлеб')
# print(some_list)

count = some_list.count('хлеб')
print(count)

last_item = some_list.pop() #без указания индекса удаляет последий элемент списка
print(last_item)
print(some_list)
other_item = some_list.pop(3) #должен удалить бублик
print(other_item)
print(some_list)

# some_list.clear()
# print(some_list)

some_list.sort(reverse=True)
print(some_list) #в чем отличие от sorted()?

some_list_copy = some_list.copy()
print(some_list_copy.clear())
print(some_list)