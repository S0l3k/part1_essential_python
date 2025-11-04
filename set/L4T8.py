# Создайте множество, содержащее другие множества
# Поскольку обычные множества не могут содержать другие множества (т.к. они изменяемы),
# используйте frozenset. Создайте несколько frozenset и объедините их в одном множестве

set_of_sets = {}
first_frozen_set = frozenset('first_frozen_set')
print(first_frozen_set, ' - первый frozenset')
second_frozen_set = frozenset('second_frozen_set')
print(second_frozen_set, ' - второй frozenset')

set_of_sets = first_frozen_set | second_frozen_set
print(set_of_sets, ' - множество со множествами')