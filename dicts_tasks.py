points_for_letters = {1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 
               'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
            2:['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
            3:['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
            4:['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
            5:['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
            8:['J', 'X', 'Ш', 'Э', 'Ю'],
            10:['Q', 'Z', 'Ф', 'Щ', 'Ъ']}

def scrabble(inp_str) -> int:
    """На вход получает строку, разбивает её на символы и суммирует значения ключей"""

    sum_points = 0

    upper_case = inp_str.upper()
    split_string = [char for char in upper_case]

    for letter in split_string:
        if letter in points_for_letters.values():
            sum_points += points_for_letters.keys(letter)
        else:
            print('Символы что вы указали несчитаются!')
    print(f'Сумма очков: {sum_points}!')

user_string = str(input('Введите текст и узнайте сколько баллов вы за это получите: '))

scrabble(user_string)