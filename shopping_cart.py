#Создать корзину с покупками
#Создать ф-цию, которая предлагает действия с корзиной "Добавить товар", "Удалить товар", "Закрыть корзину"

shopping_cart = []

def delete_item_in_shopping_cart(cart: list) -> list:
    """Выводит список товаров в корзине. Получает название товара, который необходимо удалить из корзины."""

    if not cart:
        print('Корзина пуста!')
        return cart
    
    print(f'В корзине: {cart}')
    remove_item = str(input('Введите название товара, который хотите удалить: '))
    
    if remove_item in cart:
        cart.remove(remove_item)
        print(f'Корзина состоит из: {cart}')
    else:
        print('Такого товара нет в корзине!')

    return cart


def add_item_in_shopping_cart(item_name: str, cart: list) -> list:
    """Добавляем товар в существующий список корзины"""

    # shopping_cart: list[str] = []
    cart.append(item_name)
    
    return cart



def action_with_shopping_cart(action: int) -> None:
    """На входе получаем  параметр с типом int и вызываем нужную ф-цию"""

    global shopping_cart #Создаем корзину один раз

    if action == 1:
        stop = True
        # cart = None

        while stop:
            item = str(input('Введите название товара, который хотите добавить в корзину (Если закончили добавлять товар, введите "1"): '))
            if item == '1':
                stop = False
            else:
                shopping_cart = add_item_in_shopping_cart(item, shopping_cart)
        print(f'Ваша корзина состоит из:\n {shopping_cart}\n')
    elif action == 2:
        shopping_cart = delete_item_in_shopping_cart(shopping_cart)
    elif action == 3:
        pass
    else:
        print('Вы ошиблись с выбором возможного действия!\n Попробуйте ещё раз.')

while True:
    user_action = int(input('Выберите действие, которое хотите совершить:\n' \
    '1. Нажмите "1" чтобы добавить товар в корзину.\n' \
    '2. Нажмите "2" чтобы удалить товар из корзины.\n' \
    '3. Нажмите "3" чтобы закрыть корзину.\n'))

    if user_action == 3:
        print('Программа завершина!')
        break
    else:
        action_with_shopping_cart(user_action)