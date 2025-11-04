# Напишите функцию, которая принимает строку и возвращает:
# - количество уникальных символов
# - сами уникальные символы
# Пример: "hello" → 4 уникальных символа: {'h', 'e', 'l', 'o'}

input_string = 'hello'

def unique_symbol_in_sting(input_str):
    """Принимает строку, возвращает кол-во уникальных символов и сами символы"""

    str_to_set = set(input_str)
    len_set = len(str_to_set)
    return print(f'Кол-во уникльных символов {len_set}, сами уникальные символы {str_to_set}')

unique_symbol_in_sting(input_string)