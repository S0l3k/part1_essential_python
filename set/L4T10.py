# Дан список чисел. Найдите все пары чисел, 
# сумма которых равна заданному числу target.
# Используйте множества для оптимизации поиска (O(n) вместо O(n²))
# Пример: numbers = [1, 2, 3, 4, 5, 6], target = 7
# Результат: [(1, 6), (2, 5), (3, 4)]

numbers = [1, 2, 3, 4, 5, 6]
target = 7

pairs_are_equal_to_the_target = set()
list_of_pairs_equal_to_the_target = list()

for first_value in numbers:
    second_value = target - first_value
    
    if second_value in pairs_are_equal_to_the_target:
        pair = (min(first_value, second_value), max(first_value, second_value))
        
        if pair not in list_of_pairs_equal_to_the_target:
            list_of_pairs_equal_to_the_target.append(pair)
    
    pairs_are_equal_to_the_target.add(first_value)
        
print(list_of_pairs_equal_to_the_target)