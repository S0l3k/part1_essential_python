# Даны два списка слов:
# list1 = ["apple", "banana", "orange", "grape"]
# list2 = ["banana", "kiwi", "orange", "mango"]
# Найдите слова, которые встречаются в обоих списках

list1 = ["apple", "banana", "orange", "grape"]
list2 = ["banana", "kiwi", "orange", "mango"]

set_list1 = set(list1)
set_list2 = set(list2)

general_values = set_list1 & set_list2
general_list_values = list(general_values)
print(general_list_values, ' - слова, которые встречаются в обоих списках')