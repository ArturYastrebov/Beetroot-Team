# users = []
# {
#     {
#         good: apple
#         cate
#     }
# }
#
# def hello():
#     name = input("What is your name?")
#     users.append(name)
#
# hello()
# print(users)
import copy

goods = [  {
    "category": "foods",
    "product": "burgers",
    "price": "25",
    "description": "Juicy beef burgers served with fries and barbecue sauce",
    "items": "10"
  },
{
    "category": "foods",
    "product": "salad",
    "price": "10",
    "description": "Fresh Vegetable Salad",
    "items": "10"
  },
    {
    "category": "drinks",
    "product": "tea",
    "price": "5",
    "description": "Milk oolong with spicy aroma",
    "items": "10"
  },
    {
    "category": "drinks",
    "product": "lemonade",
    "price": "5",
    "description": "Fresh lemonade with ice",
    "items": "10"
  },
    {
    "category": "hygiene",
    "product": "shampoo",
    "price": "30",
    "description": "Japanese shampoo with green tea flavor",
    "items": "10"
  },
    {
    "category": "hygiene",
    "product": "toothpaste",
    "price": "30",
    "description": "Korean toothpaste, excellent against tooth decay",
    "items": "10"
  }
]

# exit_and_cart_id = {'1': 'Banana', '2': 'another banana', '9': "Cart", '0': 'Exit'}
# key = exit_and_cart_id.keys()
# print(list(key))
# print(type(key))
categories_list = [item for item in goods if item["category"] == "hygiene"]
list_without_category = [item for item in goods if item["category"] != "hygiene"]

print(goods)
print(len(goods))
print(categories_list)
print(len(categories_list))
print(list_without_category)
print(len(list_without_category))
new_list = copy.deepcopy(list_without_category)
print(new_list)
def minus_1(new_list):
    count_shop = int(new_list[0]['items'])
    print(count_shop)
    count_shop = count_shop - 1
    new_list[0]['items'] = str(count_shop)
    return(new_list)
print(minus_1(new_list))
print(minus_1(new_list))
print(minus_1(new_list))
print(list_without_category)
# print(f'Ви отримали: {goods[1]["product"]}')


# foods_id = {
#     "1":"burgers",
#     "2":"salad",
#     "3":"tea"
# }
# cart = []
# choice = input('Choice the produkt:\n 1-"burgers"\n 2-"salad"\n 3-"tea"\n')
# # if choice == "1":
# #     cart.append(goods[0])
# # if choice == "2":
# #     cart.append(goods[1])
# # if choice == "3":
# #     cart.append(goods[2])
# for good in goods:
#     # print(good)
#     if good["product"] == foods_id[choice]:
#         cart.append(good)
# print(cart)


# print(f'Ви отримали: {cart}')