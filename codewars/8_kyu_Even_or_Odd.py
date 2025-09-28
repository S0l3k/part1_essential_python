def even_or_odd(number = int) -> None:

    if number % 2 == 0:
        print('"Even"')
    else:
        print('"Odd"')


print(even_or_odd(1))
print(even_or_odd(2))
print(even_or_odd(-1))
print(even_or_odd(-2))
print(even_or_odd(0))
