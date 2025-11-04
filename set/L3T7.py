# Напишите функцию, которая принимает два текста и возвращает:
# - слова, которые есть в обоих текстах
# - слова, которые есть только в первом тексте
# - слова, которые есть только во втором тексте
# Тексты предварительно разбейте на слова и приведите к нижнему регистру

def split_and_lower_case_string(input_str) -> list:
    """Разбивает строку на слова и приводит к нижнему регистру"""

    lower_case_string = input_str.lower()
    list_words = lower_case_string.split()

    return list_words

def word_which_be_in_text(text1, text2):
    """Сосал?"""

    list1 = split_and_lower_case_string(text1)
    list2 = split_and_lower_case_string(text2)

    in_both_texts = set(list1) & set(list2)
    print('В обоих текстах есть слова - ', in_both_texts)

    only_in_the_first_text = set(list1) - set(list2)
    print('Cлова, которые есть только в первом тексте - ', only_in_the_first_text)

    only_in_the_second_text = set(list2) - set(list1)
    print('Cлова, которые есть только во втором тексте - ', only_in_the_second_text)

first_text = 'Напишите функцию, которая принимает два текста и возвращает: Сосал?'
second_text = 'Напишите функцию, которая принимает два текста и возвращает: ' \
'- слова, которые есть в обоих текстах'

word_which_be_in_text(first_text, second_text)