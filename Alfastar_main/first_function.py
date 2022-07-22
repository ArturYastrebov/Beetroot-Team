# users_2 = (
#     {"id": "42452", "name": "Bingo", "balance": "4000", "spent": "5000", "level": "2", "kills": "4"},
#     {"id": "5341", "name": "LacasaDePapel", "balance": "42600", "spent": "97400", "level": "40", "kills": "100"},
#     {"id": "435232353", "name": "Diablo", "balance": "48888", "spent": "0", "level": "3", "kills": "2"},
#     {"id": "424", "name": "Jambo", "balance": "4000", "spent": "24552", "level": "12", "kills": "4"},
#     {"id": "5321", "name": "CoroZi", "balance": "4200", "spent": "1000", "level": "2", "kills": "1"},
#     {"id": "242432", "name": "Raynor", "balance": "720500", "spent": "0", "level": "353", "kills": "440"},
# )


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
    ("12", "Movisyan-23", "4200", "1000", "0", "2", "1"),
    ("13", "GlobalLogic", "720500", "353", "440")
)


#new_list = [list(user) for user in users_2.index()]
# print(new_list)
# print(list(users_2[0]))
# print(type(users_2[0]))
if type(users_2[0]) == tuple:
    print('users is class "tuple"')
    result = [list(user) for user in users_2]
    # print(result)

elif type(users_2[0]) == dict:
    result = []
    print('users is class "dict"')

    for user_dict in users_2:
        # print(user_dict.keys())
        newlist = [value for value in user_dict.values()]
        list_of_keys = [key for key in user_dict.keys()]
        result.append(newlist)
        # print(newlist)
    # print(result)
    # print(list_of_keys)
    result = [list_of_keys] + result
# print(new_list)
print(result)
