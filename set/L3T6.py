# Дан список чисел от 1 до N, но одно число пропущено
# numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]  # пропущено 5
# Найдите пропущенное число с помощью множеств

numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
required_numbers = len(numbers) + 1
required_list = []

for i in range(required_numbers):
    required_list.append(i+1) # добавляю 1, так как начинается с 0
print(required_list)

missing_number = set(numbers) ^ set(required_list)
print(missing_number)