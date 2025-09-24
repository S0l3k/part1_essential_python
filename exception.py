#Исключение - это не ошибка, а механизм управления потоком выполнения
#Никогда не игнорируй исключения молча (используй логирование)

a = 1
b = 0
c = "12345"
d = {1:1, 2:2, 3:3}

def test(number1: int, number2: int) -> int:
    return number1 + number2

try:
    sum = int(a + c)
except TypeError as e:
    print(f'У вас разные типы данных, их нельзя сложить арифметически.', e)

try:
    division = a/b
except ZeroDivisionError as e:
    print(f'На ноль делить нельзя.', e)

try:
    test(a, c)
except TypeError as e:
    print(f'Разный тип данных.', e)

try:
    test(c[4], a)
except TypeError as e:
    print(f'Разный тип данных.', e)

try:
    print(c[5])
except IndexError as e:
    print(f'Значения нет в строке', e)

try:
    print(d[4])
except KeyError as e:
    print(f'Значения нет в словаре под данным ключем', e)