#Создать корзину с покупками
#Создать ф-цию, которая предлагает действия с корзиной "Добавить товар", "Удалить товар", "Закрыть корзину"

user_action = int(input('Выберите действие, которое хотите совершить:\n' \
'1. Нажмите "1" чтобы добавить товар в корзину.\n' \
'2. Нажмите "2" чтобы удалить товар из корзины.\n' \
'3. Нажмите "3" чтобы закрыть корзину.\n'))

def add_item_in_shopping_cart(item_name: str, shopping_cart: list) -> list:
    """Добавляем товар в существующий список корзины"""

    # shopping_cart: list[str] = []
    shopping_cart.append(item_name)
    
    return shopping_cart



def action_with_shopping_cart(action: int) -> None:
    """На входе получаем  параметр с типом int и вызываем нужную ф-цию"""

    if action == 1:
        stop = True
        # cart = None
        shopping_cart = [] #Создаем корзину один раз

        while stop:
            item = str(input('Введите название товара, который хотите добавить в корзину (Если закончили добавлять товар, введите "1"): '))
            if item == '1':
                stop = False
            else:
                shopping_cart = add_item_in_shopping_cart(item, shopping_cart)
        print(f'Ваша корзина состоит из:\n {shopping_cart}\n')
    elif action == 2:
        pass
    elif action == 3:
        pass
    else:
        print('Вы ошиблись с выбором возможного действия!\n Попробуйте ещё раз.')

action_with_shopping_cart(user_action)