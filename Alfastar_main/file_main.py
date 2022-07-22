from pprint import pprint

from p import users_3 as users


# Приймаємо дані в листі або словнику і повертаємо змінну users в форматі лист
def date_transform_to_list_users(users_2):
    if type(users_2[0]) == tuple:
        print('users is class "tuple"')
        result = [list(user) for user in users_2]
        return result

    elif type(users_2[0]) == dict:
        result = []
        for user_dict in users_2:
            newlist = [value for value in user_dict.values()]
            result.append(newlist)
        list_of_keys = [key for key in users_2[0].keys()]
        result = [list_of_keys] + result
        return result


# Обробка даних в форматі лист, повертаємо оновлений лист
def input_users_and_creat_new_list(users):
    newlist = []
    for user in users:

        if user[0] == 'id':
            continue

        user = list(user)
        id, name, balance, spent, level, kills = user
        max_balans = (int(kills) + int(level)) * 1000
        if int(balance) != (max_balans - int(spent)):
            user[2] = str(max_balans - int(spent))
        newlist.append(user)

    newlist = [list(users[0])] + newlist
    return (newlist)


def set_type_users():  # Вибираємо тип вихідних даних
    return input('set type of users. print "1"=tuple or "2"= dict\n')


def get_users_as_tuple(users):  # перетвонення вихідних даних в tuplе
    return tuple([tuple(user) for user in users])


def get_users_as_dict(users):  # перетвонення вихідних даних в dict
    new_tuple = []
    list_of_keys = users[0]
    for user in users[1:]:
        new_dict = dict(zip(list_of_keys, user))
        new_tuple.append(new_dict)
    return tuple(new_tuple)


transformed_list = date_transform_to_list_users(users)
new_list = input_users_and_creat_new_list(transformed_list)
if set_type_users() == '1':
    pprint(get_users_as_tuple(new_list))
else:
    pprint(get_users_as_dict(new_list))
