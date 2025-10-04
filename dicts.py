p_dict = {'Филипп': 10, 'Кирилл': 25, 'Олег': 37, 'Пантелимон': 90, 'Марк': 432}

print(p_dict.keys())
print(p_dict.get('Олег'))

p_dict_items = p_dict.items()
print(p_dict_items)

p_dict_copy = p_dict.copy()
print(p_dict_copy)
print(f'К словарю p_dict_copy, применил ф-цию clear - {p_dict_copy.clear}')

print(len(p_dict))

print(p_dict.get('Марк', 'Такого ключа нет в словаре!'))
print(p_dict.get('Дмитрий', 'Такого ключа нет в словаре!'))

o_dict = {'Марк': 99, 'Древний': 666, 'Старость': 1000}
print(f'Второй словарь: ', o_dict)
print(f'Первый словарь: ', p_dict)
# n_dict = p_dict | o_dict #Значение с ключем Марк перезаписалось
# print('Третий словарь (создан из первого + второго): ', n_dict)
# p_dict |= o_dict
# print('Обновил словарь p_dict: ', p_dict)
o_dict |= p_dict
print('Обновил словарь o_dict: ', o_dict)