#метод open() - открывает файл
#метод read() - читает содержимое файла
#метод write() - записывает информацию в файл
#метод close() - закрывает файл 


# f = open('text_file.txt', 'r')
# print(*f) # * позволяет выводи содежимое файла
# f.close()

# with open('text_file.txt', 'r') as file:
#     for line in file:
#         print(line)

# file_name = 'text_file.txt'
# with open(file_name, encoding='utf8') as file:
#     print(file.read())

# with open('text_file.txt', 'w+', encoding='utf8') as file:
#     file.write('Строка 1\nСтрока 2\nСтрока 3')
#     content = file.read()
#     print(content)
#     file.seek(0)
#     content = file.read()
#     print(content)

file_name = 'text_file.txt'

def write_file():
    message = input('Введит что хотите чтобы добавить это в файл.\n')
    with open(file_name, 'a') as file:
        file.write(message + '\n')

def read_file():
    with open(file_name, 'r') as file:
        for message in file:
            print(message, end='')
    print()

while(True):
    selection = int(input('1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: '))
    match selection:
        case 1: write_file()
        case 2: read_file()
        case 3: break
        case _: print('Такой команды нет. Увы)')

print('The END!')