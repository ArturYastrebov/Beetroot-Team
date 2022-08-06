import json
from pprint import pprint



def load_category_goods(filename: str) -> dict:
    with open(filename, 'r') as f:
        category_goods = json.load(f)
    return category_goods

def save_orders(data: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=3)
    # sys.exit(0)



data_path_drinks = 'data/drinks.json'
data_path_foods = 'data/foods.json'
data_path_hygiene = 'data/hygiene.json'
order_path = 'orders/order.json'

context = {"name": '', 'cart_list': []}
