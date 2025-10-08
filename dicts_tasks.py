points_for_letters = {1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 
               'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
            2:['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
            3:['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
            4:['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
            5:['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
            8:['J', 'X', 'Ш', 'Э', 'Ю'],
            10:['Q', 'Z', 'Ф', 'Щ', 'Ъ']}

letter_points = {}
for points, letters in points_for_letters.items():
    for letter in letters:
        letter_points[letter] = points

def scrabble(inp_str) -> int:
    """На вход получает строку, разбивает её на символы и суммирует значения ключей"""

    sum_points = 0

    upper_case = inp_str.upper()

    for letter in upper_case:
        if letter in letter_points:
            sum_points += letter_points[letter]
        else:
            print(f'Символы {letter} не учитывается!')
    print(f'Сумма очков: {sum_points}!')
    return sum_points

# user_string = str(input('Введите текст и узнайте сколько баллов вы за это получите: '))

# scrabble(user_string)

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

# print(emails.keys())
# print(emails.get('mgu.edu'))

# for domains, mails in emails:
#     for mail in mails:
#         print(f'{mail} + @ + {domains}')

#моё решение с использованием списка
emails_list = []

for domain in emails.keys():
    for email in emails.get(domain):
        emails_list.append(email + '@' + domain)

for address in sorted(emails_list):
    print(address)

#предлогаемое решение 
# print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep = '\n')
