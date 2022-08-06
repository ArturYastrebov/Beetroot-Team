import copy
import json
from Class_python import check_for_number



def greeting():     # Функція вітає
    name = ''
    print('Hello new client!')
    while not name.isalpha():
        name = input('Please, enter the name:').capitalize()
        if name.isalpha():
            print(f'\n Nice to meat you {name}\n\033[40m   Your welcome in \'Buffer\' shop   \033[0m ')
            return name # функія повертає ім'я
        else:
            print('Wrong typing. Try again. Please, Enter your name:')

def shop_menu(name): # функція приймає ім'я
    id_shop_manu = ['Categories', 'Cart', 'Exit']
    print(f'\n\033[40m Buffer shop \033[0m ')
    # list_input_id = [key for key,value in enumerate(id_shop_manu,start=1)]
    list_input_id = []
    for key,value in enumerate(id_shop_manu, start=1):
        print(f'{key} - {value}')
        list_input_id.append(str(key))
    number = input(f'{name}, choice the number (1-3):')
    return check_for_number(number, list_input_id, name=name)  # функія повертає вибране число


    # Перелік функій меню
    # Реалізація вибору в меню
    # Повертає число

def categories_manu(goods, name, exit_and_cart_id): # функція приймає список товарів, імя користувача
    print(f'\n\033[40m        \'Buffer\' shop        \033[0m ')
    items_goods = set([catecory["category"] for catecory in goods])
    new_input_id = {str(key): value for key, value in enumerate(items_goods, start=1)}  # Створюю словник для кнопок
    new_input_id = new_input_id | exit_and_cart_id
    list_input_id = list(new_input_id.keys())
    for key,value in new_input_id.items():
        print(f'************** \n\033[34m{key} - {value}\033[0m')
    number = input(f'{name}, choice the categories:')
    return check_for_number(number, list_input_id, name=name), new_input_id # функція повертає вибрану категорію та словник з кнопками (ключ:категорія)

# name = 'Artur'
# num, input_id = categories_manu(goods, name)
# categoreis = input_id[num]
# print(categoreis)

def look_products(goods, name, categoreis, exit_and_cart_id): # функція приймає список товарів, імя користувача, назву категорії
    input_id = {}
    print(f'\n\033[40m        \'Buffer\' shop        \033[0m ')
    print(f'\033[40m You choice category: {categoreis} \033[0m ')
    categories_list = [item for item in goods if item["category"] == categoreis]
    list_without_category = [item for item in goods if item["category"] != categoreis]
    for key, unit in enumerate(categories_list, start=1):
        print(f'**************\nWe offer you to buy: \033[34m{unit["product"]}\033[0m\nDescription: \033[34m{unit["description"]}\033[0m')
        print(f'We have \033[34m{unit["items"]}\033[0m items\nIt\'s costs: \033[34m{unit["price"]}$\033[0m\n**************')
        print(f'\033[33m {key} - add to cart: {unit["product"]}\033[0m')
        input_id[str(key)] = unit["product"]
    print("**************")
    exit_and_cart_id2 = copy.deepcopy(exit_and_cart_id)
    exit_and_cart_id2['000'] = 'Return'
    input_id = input_id | exit_and_cart_id2
    list_input_id = list(input_id.keys())
    for key, value in exit_and_cart_id2.items():
        print(f'************** \n\033[33m{key} - {value}\033[0m')
    number = input(f'{name}, choice the numbers:')
    return check_for_number(number, list_input_id, name=name), input_id, categories_list, list_without_category # функція повертає вибрану категорію та словник з кнопками (кнопка:товар), лист товарів категорії, лист без товарів категорії.

# number, input_id, categories_list, list_without_category = look_products(goods, name, categoreis)
list_cart = []
def update_to_cart(number,input_id, categories_list, list_without_category, change, list_cart):
    # update_item_cart = []
    for item in categories_list:
        print('categories_list',categories_list)
        if int(item["items"]) > 0 and item["product"] == input_id[number]:
            print(f'We add: \033[33m{input_id[number]}\033[0m in your cart')
            if list_cart == []: # корзина пуста, створюємо перший елемент в корзині
                if int(item["items"]) > 0:
                    update_item_cart = copy.deepcopy(item)
                    print('пуста + додав товар')
                    update_item_cart["items"] = str(change)
                    item["items"] = str(int(item["items"]) - change)
                    list_cart.append(update_item_cart)
                elif int(item["items"]) == 0:
                    print('the product is unavailable')
            else:  # корзина наявна
                update_list_cart = copy.deepcopy(list_cart)
                update_list_cart2 = copy.deepcopy(list_cart)
                print('update_list_cart', update_list_cart)
                tovar_v_korz = False
                for good in update_list_cart2:

                    print('ой йойойlist_cart', list_cart)
                    print('ой йойойupdate_list_cart', update_list_cart)
                    print(good,item["category"] == good["category"],'and',item["product"] != good["product"],'or',item["category"] != good["category"],'and',item["product"] != good["product"] )
                    print(item,item["category"] == good["category"],'and', item["product"] == good["product"])

                    if item["category"] == good["category"] and item["product"] == good["product"]: # оновлюємо існуючий елемент
                        print(change,type(change))
                        # змінює товар наявний в корзині
                        print('good',good)
                        # print(list_cart["items"], type(list_cart["items"]))
                        print('update_list_cart',update_list_cart)
                        good["items"] = str(int(good["items"]) + change)
                        item["items"] = str(int(item["items"]) - change)
                        print('if23', list_cart)
                        print('update_list_cart2',update_list_cart2)
                        list_cart = update_list_cart2
                        tovar_v_korz = True
                #elif item["category"] == good["category"] and item["product"] != good["product"] or item["category"] != good["category"] and item["product"] != good["product"]:  # перевірка чи є такий товав вже в корзині

                if tovar_v_korz == False:
                    print('item222', item)
                    # додає перший товар в корзину
                    update_item_cart = copy.deepcopy(item)
                    print('update_item_cart', update_item_cart)
                    update_item_cart["items"] = change
                    item["items"] = str(int(item["items"]) - change)
                    print('update_item_cart345', update_item_cart)
                    update_list_cart.append(update_item_cart)
                    print('if12', update_list_cart)
                    list_cart = update_list_cart
                print('update_list_cart', update_list_cart)
    new_goods = categories_list + list_without_category
    print('Товари в магазині :', new_goods)
    print('Товари в корзині :', list_cart)

    return(list_cart, new_goods)

# list_cart = [{'category': 'foods', 'product': 'burgers', 'price': '25', 'description': 'Juicy beef burgers served with fries and barbecue sauce', 'items': '3'}, {'category': 'foods', 'product': 'salad', 'price': '10', 'description': 'Fresh Vegetable Salad', 'items': '7'}, {'category': 'drinks', 'product': 'tea', 'price': '5', 'description': 'Milk oolong with spicy aroma', 'items': '2'}]
# new_goods = [{'category': 'foods', 'product': 'burgers', 'price': '25', 'description': 'Juicy beef burgers served with fries and barbecue sauce', 'items': '7'}, {'category': 'foods', 'product': 'salad', 'price': '10', 'description': 'Fresh Vegetable Salad', 'items': '3'}, {'category': 'drinks', 'product': 'tea', 'price': '5', 'description': 'Milk oolong with spicy aroma', 'items': '8'}]

def cart(name, list_cart, new_goods):
    print(f'\n\033[40m        \'Buffer\' shop        \033[0m ')
    print(f'\033[40m *******| Your cart |******* \033[0m ')
    id_cart_manu = ['Selected products', 'Get order', 'Clean cart']
    # list_input_id = [key for key,value in enumerate(id_shop_manu,start=1)]
    list_input_id = []
    for key,value in enumerate(id_cart_manu, start=1):
        print(f'{key} - {value}')
        list_input_id.append(str(key))
    print(f'000 - Return')
    list_input_id.append("000")
    number = input(f'{name}, choice the number (1-3 or 000):')
    return check_for_number(number, list_input_id, name=name)

def selected_products(name, list_cart, new_goods):
    print(f'\n\033[40m        \'Buffer\' shop        \033[0m ')
    print(f'\033[40m *******| You chose |******* \033[0m ')
    list_input_id = []
    for key, good in enumerate(list_cart, start=1):
        print(f'**************\n{good["product"].capitalize()} in category {good["category"]} {good["items"]} pcs')
        print(f' {key} - selected products {good["product"]}')
        list_input_id.append(str(key))
    print('99 - Delete\n000 - Return\n**************')
    list_input_id.append("000")
    list_input_id.append("99")
    number = input(f'{name}, choice the number:')
    return check_for_number(number, list_input_id, name=name), list_input_id

def selected_products_menu(number, list_cart, new_goods,name): # функція приймає ім'я
    id_shop_manu = ['Categories', 'Cart', 'Exit']
    print(f'\n\033[40m Buffer shop \033[0m ')
    # list_input_id = [key for key,value in enumerate(id_shop_manu,start=1)]
    list_input_id = []
    for key,value in enumerate(id_shop_manu, start=1):
        print(f'{key} - {value}')
        list_input_id.append(str(key))
    number = input(f'{name}, choice the number (1-3):')
    return check_for_number(number, list_input_id, name=name)  # функія повертає вибране число

def main():
    list_cart = []
    num = "0"
    bot = True
    exit_and_cart_id = {'00': "Cart", '0': 'Exit'}
    with open('../shop_bot_v2/data/hygiene.json', 'r') as items:  # Читаємо дані з файлу
        goods = json.load(items)
        name = greeting()
    while bot:
        if num != '00':
            num = shop_menu(name)
        if num == '1':
            while num != '0' and num != '00':
                num, input_id = categories_manu(goods, name, exit_and_cart_id)
                if num == '00':
                    break
                elif num == '0':
                    print(f'Good bye, {name}')
                    bot = False
                    break
                elif num in list(input_id.keys()):
                    categoreis = input_id[num]
                    while num != '000' and num != '00':
                        num, input_id, categories_list, list_without_category = look_products(goods, name, categoreis, exit_and_cart_id)
                        if num == '00':
                            break  # korzina
                        elif num == '0':
                            print(f'Good bye, {name}')
                            bot = False
                            break
                        elif num == '000':
                            print('povernuvcya nazad')
                        elif num in list(input_id.keys()):
                            list_cart, goods = update_to_cart(num, input_id, categories_list, list_without_category, 1, list_cart)
                            print('vuhid',list_cart)
        elif num == '2' or num == '00':
            num = cart(name, list_cart, goods)  # korzina
            if num == '1':
                num, list_input_id = selected_products(name, list_cart, goods)
                if num == '99':
                    pass
                elif num == '000':
                    pass
                elif num in list(list_input_id):
                    print(list_input_id)
            elif num == '2':
                pass


        elif num == '3':
            print(f'Good bye, {name}')
            break


main()

    # intup number
    # При натисканні юзер бачить інформацію про товар
    # Delete product
    # Return
    # Повертає число

def get_order():
    pass
    # intup number
    # виводить список товарів, тотал прайс і меню
    # Next
    # return
    # Повертає число
    # confirm


def total_price():
    pass
    # загальна ціна товарів




# меню:
#     категорії:
#
#         косметика:
#         їжа:
#             (опис товару)
#
#             додати в корзину:
#                 (напис що додано)
#                 повертає попереднє меню
#
#             корзина
#                 отримати замовлення
#
#             повернутися в основне меню
#             вихід
#
#         корзина:
#         вихід
#     корзина:
#     вихід

