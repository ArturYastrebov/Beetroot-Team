users_2 = (
    ("id", "name", "balance", "spent", "level", "kills"),
    ("1", "Bilbo", "4000", "5000", "2", "4"),
    ("2", "Indigo", "42600", "97400", "40", "100"),
    ("3", "Farmer", "5000", "0", "3", "2"),
    ("4", "O'rizotto", "5000", "0", "1", "0"),
    ("5", "Bilbo-1", "0", "0", "1", "0"),
    ("6", "Bilbo-2", "0", "0", "1", "0"),
    ("7", "Bilbo-3", "0", "0", "1", "0"),
    ("8", "O'rizotto-1", "0", "0", "1", "0"),
    ("9", "O'rizotto-2", "0", "0", "1", "0"),
    ("10", "O'rizotto-3", "0", "0", "1", "0"),
    ("11", "O'rizotto-4", "0", "0", "1", "0"),
    ("12", "Movisyan-23", "4200", "1000", "2", "1"),
    ("13", "GlobalLogic", "720500", "0", "353", "440"))


# Приймаємо дані в листі або словнику і повертаємо змінну users в форматі лист
def date_transform_to_list_users(users_2):
    if type(users_2[0]) == tuple:
        # print('users is class "tuple"')
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


# Оновлення балансу юзерів
def update_balance(users):
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

    print(newlist)
    return (newlist)

#  Пошук чітерів
def check_cheaters(users):
    cheaters_list = []
    for user in users:

        if user[0] == 'id':
            continue

        user = list(user)
        id, name, balance, spent, level, kills = user
        max_balans = (int(kills) + int(level)) * 1000
        if int(balance) != (max_balans - int(spent)):
            cheaters_list.append(user)
    print(cheaters_list)
    if cheaters_list != []:
        print('Cheaters are found')
        raise ValueError('Cheaters found')


# update_balance(date_transform_to_list_users(users_2))
# check_cheaters(date_transform_to_list_users(users_2))

try:
    check_cheaters(date_transform_to_list_users(users_2))
except ValueError:
    update_balance(date_transform_to_list_users(users_2))
    print('Balance Users is OK')
