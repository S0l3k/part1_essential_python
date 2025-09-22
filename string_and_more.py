test_string = 'I something write and I want what that sting help me to do question.'

#Определение длинны строки
lenght_string = len(test_string)
print(f"Кол-во символов в тестовой строке = ", lenght_string)

#Доступ по индексу
first_char = test_string[0]
second_char = test_string[1]
last_char = test_string[-1]
print(f"Первый символ тестовой строки = ", first_char, 
      "\nВторой символ тестовой строки = ", second_char, 
      "\nПоследний символ тестовой строки = ", last_char)

#Срез строки
"""
my_string[start:end], где start — индекс начала среза, а end — индекс конца (не включается).
При выходе за границы диапазона возникает ошибка IndexError.
"""
test_substring = test_string[0:6]
print(f"Подстрока = ", test_substring)

#Шаг извлечения среза
""""
my_string[start:end:step], где
start: индекс начала среза (включительно).
end: индекс конца среза (не включительно).
step: шаг между символами.
"""
every_second_char = test_string[::2] #Выводит каждый второй символ
print(every_second_char)

reversed_string = test_string[::-1] #Получение обратной строки
print(reversed_string)

test_substring_with_step = test_string[0:10:2] #Получение части строки с определенным шагом
print(test_substring_with_step)