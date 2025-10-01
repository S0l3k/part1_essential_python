def even_or_odd(number = int) -> str:

    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(even_or_odd(1))
print(even_or_odd(2))
print(even_or_odd(-1))
print(even_or_odd(-2))
print(even_or_odd(0))
