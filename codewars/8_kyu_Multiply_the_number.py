def multiply(n):
    """На входе получаю число которое нужно умножить на 5 возведенное в степень по кол-ву 
    цифр в числе"""

    n_to_abs = abs(n)
    n_to_str = str(n_to_abs)
    n_len = len(n_to_str)
    degree = int(n_len)

    return n * (5**degree)

print(multiply(10))
print(multiply(5))
print(multiply(200))
print(multiply(0))
print(multiply(-2))

# enter_number = 1245
# enter_number_to_str = str(enter_number)
# size_enter_number = len(enter_number_to_str)
# print(size_enter_number)