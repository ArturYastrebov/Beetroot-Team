# Привітання, запитує ім'я користовача <-> greeting()
# 0.Розділи меню  <-> shop_menu()

# 1.Категорії
#     1.1 Категорії товарів
#         1.1.1 Опис товару категорії
#         1.1.2 Додати товар у корзину
#         1.1.3 Корзина
#             1.1.3.1 Опис товару в кошику
#             1.1.3.2 Редагування корзини
#                 1.1.3.2.1 Видалити певну кількість продукту
#                 1.1.3.2.2 Очистити корзину
#                 1.1.3.2.3 Повернутися назад
#                 1.1.3.2.4
#             1.1.3.3 Отримати замовлення
#                 1.1.3.3.1 Список товарів та ціна
#                 1.1.3.3.2 Підтвердити замовлення
#                     1.1.3.3.2.1 Введіть адресу доставки та додаткову інформацію по доставці.
#                         1.1.3.3.2.1.1 Заказ сформовано. Дякую.
#                 1.1.3.3.3 Повернутися в попереднє меню
#             1.1.3.4 Попереднє меню
#             1.1.3.5 Вихід
#         1.1.4 Попереднє меню
#         1.1.5 Вихід
#     1.2 Попереднє меню
#     1.3 Вихід
# 2.Корзина
# 3.Вихід
import copy
import sys
from pprint import pprint

from Class_python.shop_bot_v2.utils import context, data_path_drinks, load_category_goods, data_path_foods, \
    data_path_hygiene


def greeting(context):     # Привітання, запитує ім'я користовача
    print('Hello new client!')
    while not context["name"].isalpha():
        context["name"] = input('\033[33mPlease, enter the name:\033[0m').capitalize()
        if context["name"].isalpha():
            print(f'\n Nice to meat you {context["name"]}\n\033[40m   Your welcome in \'Buffer\' shop   \033[0m ')
            shop_menu(context)
        else:
            print('\033[31mWrong typing. Try again. Please, Enter your name:\033[0m')
# greeting(context)
# print(context)
def read_drinks_file(context):
    if ["drinks_goods_list"] is not context:
        context["drinks_goods_list"] = load_category_goods(data_path_drinks)
        context['swich_categorys'] = 'drinks'
    return show_goods(context)

def read_foods_file(context):
    if ["foods_goods_list"] is not context:
        context["foods_goods_list"] = load_category_goods(data_path_foods)
        context['swich_categorys'] = 'foods'
    return show_goods(context)

def read_hygiene_file(context):
    if ["hygiene_goods_list"] is not context:
        context['hygiene_goods_list'] = load_category_goods(data_path_hygiene)
        context['swich_categorys'] = 'hygiene'
    return show_goods(context)


def print_goods(context, list_goods, batton = True, delate = False):
    total_price = 0
    context["delate"] = {}
    for key, unit in enumerate(list_goods, start=1):
        print(f'**************\nName of product: \033[34m{unit["product"]}\033[0m')
        if batton: print(f'Description: \033[34m{unit["description"]}\033[0m')
        print(f'We have \033[34m{unit["items"]}\033[0m items\nIt\'s costs: \033[34m{unit["price"]}$ for 1 pc\033[0m\n**************')
        if batton and not delate: print(f'\033[33m {key} - add to cart: {unit["product"]}\033[0m')
        else:
            print(f'\033[33m Total price = {int(unit["items"])}x{int(unit["price"])} = {int(unit["items"])*int(unit["price"])}$\033[0m')
            total_price += int(unit["items"])*int(unit["price"])
        if delate:
            print(f'\033[33m {key} - subtract from cart: {unit["product"]}\033[0m')
            context["delate"][key] = unit["product"]
    if not batton: print(f'\033[36m--->>> All goods cost:{total_price}$ <<<---\033[0m')
    return total_price

def check_swich_categorys(context):
    if context['swich_categorys'] == 'drinks':
        list_goods = context["drinks_goods_list"]
    elif context['swich_categorys'] == 'foods':
        list_goods = context["foods_goods_list"]
    elif context['swich_categorys'] == 'hygiene':
        list_goods = context["hygiene_goods_list"]
    return list_goods


def show_goods(context):
    print('We offer you to buy a fresh goods:')
    list_goods = check_swich_categorys(context)
    print_goods(context,list_goods, batton=True)
    main_menu = {
        "C": {"handler": show_cart_menu, "description": "Show cart"},
        "R": {"handler": show_categories_manu, "description": "Return"},
        "0": {"handler": exit, "description": "Exit"},
    }
    print_menu(main_menu)
    check_input(context, main_menu, list_goods)



def show_categories_manu(context):
    main_menu = {
        "1": {"handler": read_drinks_file, "description": "drinks"},
        "2": {"handler": read_foods_file, "description": "foods"},
        "3": {"handler": read_hygiene_file, "description": "hygiene"},
        "C": {"handler": show_cart_menu, "description": "Show cart"},
        "R": {"handler": shop_menu, "description": "Return"},
        "0": {"handler": exit, "description": "Exit"},
    }
    print_menu(main_menu)
    check_input(context, main_menu)

def get_orders(context):
    print('You in get_orders')


def change_product_in_cart(context):
    print('You in change_product_in_cart')
    print_goods(context ,context["cart_list"], delate = True)
    print('111')
    # list_goods = check_swich_categorys(context)
    # update_to_cart(context, list_goods, change=-1)
    check_input(context, main_menu)


def show_cart_menu(context):
    print('You in show_cart_menu')
    if len(context["cart_list"]) != 0:
        total_price = print_goods(context, context["cart_list"], batton=False)
        main_menu = {
            "1": {"handler": change_product_in_cart, "description": "Change products"},
            "2": {"handler": get_orders, "description": "Get orders"},
            "R": {"handler": shop_menu, "description": "Return"},
            "0": {"handler": exit, "description": "Exit"},
        }
        print_menu(main_menu)
        check_input(context, main_menu)
    print(f'\033[31mYour cart is empty.{context["name"]},pleace, choce the products\033[0m')
    shop_menu(context)

def exit(context):
    print('Bye')
    sys.exit(0)

def print_menu(main_menu):
    for key, value in main_menu.items():
        print(f' {key} - {value["description"].capitalize()}')

def update_to_cart(context, list_goods, change=1):
    print('I am in update_to_cart')
    for item in list_goods:
        if item['product'] == context['product to cart'] and int(item['items']) >= change:
            item['items'] = str(int(item["items"]) - change)
            check_good_in_cart = False
            for good_context in context['cart_list']:
                if context['product to cart'] == good_context["product"]:
                    good_context["items"] = str(int(good_context["items"]) + change) #оновили товар у кошику
                    check_good_in_cart = True
            if check_good_in_cart == False:
                update_item_cart = copy.deepcopy(item)
                update_item_cart["items"] = change
                context["cart_list"].append(update_item_cart)
    return show_goods(context)


# def check_items(list_goods):
#     for good in list_goods:
#         good['items']

def check_input(context,main_menu,list_goods=[]):
    while 1:
        action = input(f'\033[33m{context["name"]}, put the number: \033[0m').upper()
        if action in main_menu:
            return main_menu[action]["handler"](context)
        elif int(action) in list(range(len(list_goods)+1)):
            context["product to cart"] = list_goods[int(action)-1]['product']
            return update_to_cart(context,list_goods)
        else:
            print('\033[31mIncorrect command!\033[0m')


def shop_menu(context):  # 0.Розділи меню
    main_menu = {
        "1": {"handler": show_categories_manu, "description": "Categories"},
        "C": {"handler": show_cart_menu, "description": "Show cart"},
        "0": {"handler": exit, "description": "Exit"}
    }
    print_menu(main_menu)
    check_input(context, main_menu)



greeting(context)


# def handle_1(context):
#     print(context["user_name"])
#
# def handle_2(context):
#     print(context["cart"])
#
# def shop_menu(context)
# main_menu = {
#     "1": {"handler": handle_1, "description": "Show user name"},
#     "2": {"handler": handle_2, "description": "Show cart"},
# }
#
# context = {"user_name": "admin", "cart": ["apple", "banana"]}
#
# main_menu["1"]["handler"](context)
# main_menu["2"]["handler"](context)
#
# data = {"product": "apple", "price": 10}