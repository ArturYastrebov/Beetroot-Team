import copy
import json
import datetime
import re
import string
import random
import sys


from utils import INPUT_USERS, INPUT_APARTMENTS, save_data_to_json_file, \
    parse_data_form_json_file, OUTPUT_APARTMENTS, OUTPUT_USERS


data_users = parse_data_form_json_file(INPUT_USERS)
data_apartments = parse_data_form_json_file(INPUT_APARTMENTS)
print(data_users, '\n', data_apartments)
info = {"login":'', "apart":'', "start_date_booking":'',"free_time_zones":'', 'end_date_booking':'', 'return_to_bokking': False, 'count_of_people':'', 'max_money':''}


def greeting():
    while 1:
        user_said = input(
            '\033[1;34mWelcome to the booking apartments\nHave you ever been here before? Yes(Y)/NO(N) or (0)Exit\033[0m ').upper()
        actions = {'N': add_new_users, 'Y': check_login, '0': sys.exit}
        argum = {'N': data_users, 'Y': data_users, '0': 0}
        actions[user_said](argum[user_said]) if user_said in actions else print(
            '\033[1;31mIncorrect value, please try again:\033[0m')


def load_data_users(path_data: str) -> dict:
    with open(path_data, "r") as f:
        data_users = json.load(f)
        return data_users


def update_data_users(path_data: str, data_users: dict):
    with open(path_data, 'w') as f:
        json.dump(data_users, f, indent=4)


def input_positive_num(text_search):
    while 1:
        try:
            num = input(f"Please, enter {text_search}: ")
            if int(num) > 0:
                return num
            print(f"The {text_search} must be greater than 0")
        except ValueError:
            print("Wrong type format!!!")


def check_login(data_users):
    while 1:
        login = input('\033[1;34mEnter your login or return(R): \033[0m')
        if login.upper() == "R":
            greeting()
        elif login in data_users.keys():
            while 1:
                pasword = input("\033[1;34mEnter password or return(R): \033[0m")
                if pasword.upper() == 'R':
                    break
                elif pasword != data_users[login]["password"]:
                    print(f'\033[1;31mWrong password for login {login}, try again\033[0m')
                else:
                    print(
                        f'\033[1;34mYou are welcome, {data_users[login]["name"]} {data_users[login]["second_name"]}\033[0m')
                    return main_menu(data_apartments, login)
        else:
            print(f'\033[1;31mSorry, we dont have any users wich login is {login}\033[0m')


def input_login(data_users):
    print('\033[1;34mHello new Usesr!\033[0m')
    while 1:
        login = input('\033[1;34mEnter your login or return(R): \033[0m')
        if login.upper() == "R":
            return greeting()
        elif re.search(r'[!@#$%^&+=]', login) is not None:
            print('\033[1;31mlogin mustn\'t contain special symbol\033[0m')
        elif (len(login) < 6 or len(login) > 20):
            print('\033[1;31mlogin must be from 6 to 20 characters long\033[0m')
        elif login in data_users.keys():
            print('\033[1;31mBooking system has the same login\033[0m')
        else:
            return login


def input_name_or_second_name(word):
    while 1:
        login = input(f'\033[1;34mEnter your {word} or return(R): \033[0m').capitalize()
        if login.upper() == "R":
            greeting()
        elif re.search(r'[!@#$%^&+=]', login) is not None:
            print(f'\033[1;31m{word} mustn\'t contain any special symbol\033[0m')
        elif re.search(r'\d', login) is not None:
            print(f'\033[1;31m{word} mustn\'t contain any digit\033[0m')
        else:
            return login


def input_password():
  while 1:
    password = input('\033[1;34mpassword :\033[0m')
    if (len(password) < 8 or len(password) > 20):
      print('\033[1;31mpassword must be from 8 to 20 characters long\033[0m')
    elif re.search(r'[!@#$%^&+=]', password) is None:
      print('\033[1;31mpassword must contain atleast one special symbol\033[0m')
    elif re.search(r'\d', password) is None:
      print('\033[1;31mpassword must contain atleast one digit\033[0m')
    elif re.search('[A-Z]', password) is None:
      print('\033[1;31mpassword must contain atleast one capital letter\033[0m')
    elif re.match(r'[a-z A-Z 0-9 !@#$%^&+=]{8,20}', password):  # перевірити на пробіли в паролі
      print('\033[1;34mYou created a strong password=)\033[0m')
      return password
    else:
      print('\033[1;31mpassword invalid\033[0m')


def create_password():
  while 1:
    print("\033[1;34mCreate strong password\033[0m")
    password = input_password()
    second_password = input('\033[1;34mPleace, repead your password:\033[0m')
    if password == second_password:
      print('\033[1;34mSuccess!!! Password was created!!!\033[0m')
      return password
    else:
      print('\033[1;31mYou entered two different password. Try again.\033[0m')


def generator_password():
    combination = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(10):
        password += combination[random.randint(0, len(combination) - 1)]
    print(f'\033[1;34mGreat! Your password is: {password}\033[0m')
    return password


def registration(data_users, info_user):
    info_user["login"] = input_login(data_users)
    user_said = input('\033[1;34mWould you like to generate password? yes(Y) or no(N)\033[0m').upper()
    info_user["password"] = ''
    while not info_user["password"]:
        if user_said == "Y":
            info_user["password"] = generator_password()
        elif user_said == "N":
            info_user["password"] = create_password()
        else:
            print('\033[4;31Incorrect value, please try again:\033[0m')
    info_user["name"] = input_name_or_second_name("name")
    info_user["second_name"] = input_name_or_second_name("second name")
    return data_users, info_user


def save_login_to_json(data_users, info_user):
    login = info_user["login"]
    data_users[login] = {"password": info_user["password"], 'name': info_user["name"], "second_name": info_user["second_name"], "balance": '0'}
    print(
        f'\033[1;34mAccount has been created!!! You are welcome, {data_users[login]["name"]} {data_users[login]["second_name"]}\033[0m')
    save_data_to_json_file(OUTPUT_USERS, data_users)
    info['login'] = login
    return main_menu(data_apartments, info['login'])


def print_new_users(info_user):
    print("\033[1;34mCheck your informations: \033[0m\n"
          f"\033[1;34mLogin: \033[0m{info_user['login']} \n"
          f"\033[1;34mPassword : \033[0m{info_user['password']}\n"
          f"\033[1;34mYour name: \033[0m{info_user['name']}\n"
          f"\033[1;34mYour second name\033[0m{info_user['second_name']}\n")


def add_new_users(data_users):
    info_user = {}
    registration(data_users, info_user)
    print_new_users(info_user)
    while 1:
        print("Nice job!!!")
        user_said = input('\033[1;34mEnter Confirm(Y), change(C) informations or return(R): \033[0m')
        if user_said.upper() == "R":
            greeting()
        elif user_said.upper() == "C":
            add_new_users(data_users)
        elif user_said.upper() == "Y":
            save_login_to_json(data_users, info_user)
            return main_menu(data_apartments, info_user['login'])
        else:
            print(f'\033[1;31mSorry, wrong answer, try again.\033[0m')


def main_menu(data_apartments, login):
    info['login'] = login
    print('\033[1;34mWhat do you want to do?\033[0m')
    user_said = input('\033[1;32m1 - Start booking\n'
                      '2 - Submit apartment to offer\n'
                      '3 - Update your balance\033[0m\n'
                      '\033[37m0 - Quit from menu\033[0m\n')
    if user_said == '1': return collect_input_inf(info)
    elif user_said == '2': return add_new_appart(data_apartments, info)
    elif user_said == '3':
        info['return_to_bokking'] = False
        return update_balance_set(data_users, info)
    elif user_said == '0': return greeting()
    else: print('\033[4;31mIncorrect value, please try again:\033[0m')
    return main_menu(data_apartments, login)


def check_str_data(str_data):
    try:
        if convert_str_to_time(str_data) <= datetime.datetime.now().date():
            raise TimeoutError
    except TimeoutError:
        print('\033[31mYou have selected a date in the past,try again\033[0m')
    except Exception:
        print('\033[31mIncorrect format data,try again\033[0m')
    else:
        print('Correct format data')
        return True


def input_date():
    check_data = False
    while not check_data:
        date_booking = f'{input("day: ")}.{input("month: ")}.{input("Year: ")}'
        check_data = check_str_data(date_booking)
    date_booking = convert_str_to_time(date_booking)
    return date_booking, check_data


def input_search_data():
    check_data = False
    while not check_data:
        print('\033[1;34mUser,chose the date of booking:\033[0m')
        info['start_date_booking'], check_data = input_date()
        actions = input('\033[1;34mWould you like enter count of day - (D) or the last day of booking - (L) \033[0m')
        if actions.upper() == 'D':
            count_day = input('\033[1;34mEnter count of days: \033[0m')
            info['end_date_booking'] = info['start_date_booking'] + datetime.timedelta(int(count_day))
        elif actions.upper() == 'L':
            print('\033[1;34mUser,chose the last date of booking:\033[0m')
            info['end_date_booking'], check_data = input_date()
        else:
            print('\033[31mIncorrect value, please try again\033[0m')
            return input_search_data()
        if info['start_date_booking'] > info['end_date_booking']:
            check_data = False
            print('\033[31mOMG!!! start_date_booking > end_date_booking, try again.\033[0m')
    return info['start_date_booking'], info['end_date_booking']


def collect_input_inf(info):
    info['count_of_people'] = input_count_of_people()
    info['max_money'] = input_count_of_max_money()
    info['start_date_booking'], info['end_date_booking'] = input_search_data()
    return show_apartment(data_apartments, info)


def input_count_of_people():
    while 1:
        count_of_people = input('\033[1;34mUser,how many people will live in the apartments? \033[0m')
        if count_of_people.isdigit():
            if int(count_of_people) > 0:
                return int(count_of_people)
        print("\033[31mOMG!!!Incorrect value, please try again\033[0m")


def input_count_of_max_money():
    while 1:
        max_money = input('\033[1;34mUser,up to what amount money to search? \033[0m')
        if max_money.isdigit():
            if int(max_money) > 0:
                return int(max_money)
        print("\033[31mOMG!!!Incorrect value, please try again\033[31m")


def show_apartment(data_apartments, info):
    print(
        f'In your days >>> {convert_time_to_str(info["start_date_booking"])} - {convert_time_to_str(info["end_date_booking"])} <<< available:')
    count = 0
    key_id = {}
    for key, apartment in data_apartments.items():
        if info["count_of_people"] <= int(apartment["people"]):
            if info["max_money"] >= int(apartment["price"]):
                for info["period_time"] in apartment['free_time']:
                    if convert_str_to_time(info["period_time"][0]) <= info["start_date_booking"] and (
                            info["end_date_booking"] <= convert_str_to_time(info["period_time"][1])):
                        count += 1
                        print(
                            f'\n\033[1;7m*** {key} ***\033[0m\nUp to {apartment["people"]} people can live in the apartments\nPrice per day: {apartment["price"]}')
                        print(
                            f'Description : {apartment["description"]}\n\033[1;34m>>>> {count} <<<< press, if you want to book {key} <<<\033[0m')
                        key_id[str(count)] = key
    return choice_num_apart(key_id, info)


def choice_num_apart(key_id, info):
    while 1:
        actions = input(
            f"\n_________________________________\n\033[1;34mEnter from 1 to {len(key_id)} or Return (R)\033[0m")
        if actions.upper() == "R":
            main_menu(data_apartments, info['login'])
        elif actions.isdigit():
            if int(actions) in list(range(1, len(key_id) + 1)):
                info['apart'] = key_id[actions]
                return booking_apartment(data_apartments, info)
        print('\033[31mIncorrect value, please try again\033[0m')


def booking_apartment(data_apartments, info):
    free_time_zones = copy.deepcopy(data_apartments[info['apart']]["free_time"])
    for i, period_time in enumerate(free_time_zones):
        if (convert_str_to_time(period_time[0])) <= info['start_date_booking'] and (
                info['end_date_booking'] <= convert_str_to_time(period_time[1])):
            free_time_zones.append([period_time[0], convert_time_to_str(info['start_date_booking'])])
            free_time_zones.append([convert_time_to_str(info['end_date_booking']), period_time[1]])
            free_time_zones.pop(i)
    info['free_time_zones'] = free_time_zones
    return confirm_booking(data_apartments, data_users, info)


def print_confirm_booking(data_apartments, data_users, info):
    count_days_booking = (info['end_date_booking'] - info['start_date_booking']).days
    total_cost = count_days_booking * int(data_apartments[info['apart']]["price"])
    print(f'\033[1;34mYou choiced \033[0m{info["apart"]} '
          f'from {convert_time_to_str(info["start_date_booking"])} to {convert_time_to_str(info["end_date_booking"])}'
          f'\n\033[1;34mIt is \033[0m{count_days_booking} days'
          f'\n\033[1;34mIt cost \033[0m{total_cost}$')
    return count_days_booking, total_cost


def save_all_data(data_users, data_apartments, info):
    data_apartments[info['apart']]['free_time'] = info['free_time_zones']
    save_data_to_json_file(OUTPUT_USERS, data_users)
    save_data_to_json_file(OUTPUT_APARTMENTS, data_apartments)
    print(f"\033[1;34mYour balance is change! You have \033[0m{data_users[info['login']]['balance']}$")
    return main_menu(data_apartments, info['login'])


def add_some_money_after_booking():
    print('\033[1;31mYou don\'t have enough money\033[0m')
    actions = input('\033[1;34mWould you like to top up the card account\033[0m\n Yes(Y) or return(R)')
    if actions.upper() == 'Y':
        info['return_to_bokking'] = True
        return update_balance_set(data_users, info)
    elif actions.upper() == 'R':
        return show_apartment(data_apartments, info)
    print('\033[31mIncorrect value, please try again\033[0m')


def confirm_booking(data_apartments, data_users, info):
    while 1:
        count_days_booking, total_cost = print_confirm_booking(data_apartments, data_users, info)
        actions = input('\033[1;34mWould you like to continue booking?\033[0m\n Yes(Y) or return(R)')
        if actions.upper().upper() == 'Y':
            if int(data_users[info['login']]['balance']) >= total_cost:
                data_users[info["login"]]['balance'] = str(int(data_users[info["login"]]['balance']) - total_cost)
                print(f"\033[1;34mDone! You booked the {info['apart']} on {count_days_booking} days\033[0m")
                save_all_data(data_users, data_apartments, info)
            else:
                while 1:  add_some_money_after_booking()
        elif actions.upper() == 'R':
            return show_apartment(data_apartments, info)
        else: print('\033[31mIncorrect value, please try again\033[0m')


def convert_time_to_str(date):
    return date.strftime("%d.%m.%Y")


def convert_str_to_time(data_str):
    return datetime.datetime.strptime(data_str, "%d.%m.%Y").date()


def input_text(text_search: str, lim_min: int = 4, lim_max: int = 50) -> str:
    while 1:
        text = input(f"Please, enter {text_search}: ")
        if (len(text) < lim_min or len(text) > lim_max):
            print(f'\033[1;{text_search} must be from {lim_min} to {lim_max} characters long\033[0m')
        elif re.search(r'[!@#$%^&*)(}{\[\]+=]', text) is not None:
            print(f'\033[1;31{text_search} must\'nt contain special symbol like !@#$%^&*)([]+=\033[0m')
        elif re.search(r'[a-z A-Z 0-9 _]{4,50}', text):
            print(f'\033[1;34m{text_search} apart is correct\033[0m')
            return text
        else:  print(f'\033[1;31m{text_search} invalid\033[0m')


def create_new_apart():
    name_apart = input_text("name of apartment")
    description = input_text("description text", lim_min=30, lim_max=200)
    start_date_booking, end_date_booking = input_search_data()
    free_period = convert_time_to_str(start_date_booking), convert_time_to_str(end_date_booking)
    count_people = input_positive_num('number of guests')
    cost_per_day = input_positive_num('cost per day')
    new_apart_dict = {name_apart: {"free_time": [free_period], "description": description, "people": count_people,
                                   "price": cost_per_day}}
    return new_apart_dict, name_apart


def print_appart(new_apartments, name_apart):
    print("\033[1;34mCheck your input pleace: \033[0m\n"
          f"\033[1;34mname apartment: \033[0m{name_apart} \n"
          f"\033[1;34mdescription : \033[0m{new_apartments[name_apart]['description']}\n"
          f"\033[1;34mfree period for booking: \033[0m from {new_apartments[name_apart]['free_time'][0][0]} to {new_apartments[name_apart]['free_time'][0][1]} \n"
          f"\033[1;34mthe number of people accommodated in the apartment :\033[0m{new_apartments[name_apart]['people']}\n"
          f"\033[1;34mprice per day: \033[0m{new_apartments[name_apart]['price']}")


def add_new_appart(apartments, info):
    new_apartments, name_apart = create_new_apart()
    print_appart(new_apartments, name_apart)
    while 1:
        user_said = input('\033[1;34mEnter Confirm(Y), change(C) informations or return(R): \033[0m')
        if user_said.upper() == "R":
            return main_menu(data_apartments, info['login'])
        elif user_said.upper() == "C":
            return add_new_appart(apartments, info)
        elif user_said.upper() == "Y":
            print(f"\033[1;34mDone!!!\033[0m You added {name_apart}")
            apartments[name_apart] = new_apartments[name_apart]
            save_data_to_json_file(OUTPUT_APARTMENTS, apartments)
            return main_menu(data_apartments, info['login'])
        else:
            print(f'\033[1;31mSorry, wrong answer, try again.\033[0m')


def update_balance(data_users, login):
    while 1:
        print(f'{data_users[login]["name"]} {data_users[login]["second_name"]} you have {data_users[login]["balance"]}$')
        count_of_money = input_positive_num("count of money")
        money = input(f'\033[1;34mWould you like to add {count_of_money}$ from {login}?\033[0m\n Press yes(Y) or return(R)')
        if money.upper() == "R":
            break
        elif money.upper() == "Y":
            data_users[login]['balance'] = str(int(data_users[login]['balance']) + int(count_of_money))
            print(f'\033[1;34mSuccess!!!You added {count_of_money}$ from {login}\033[0m')
            save_data_to_json_file(INPUT_USERS, data_users)
            break
        else:
            print(f'\033[1;31mSorry, wrong answer, try again.\033[0m')


def update_balance_set(data_users, info):
    if not info['return_to_bokking']:
        update_balance(data_users, info['login'])
        return main_menu(data_apartments, info['login'])
    else:
        update_balance(data_users, info['login'])
        return confirm_booking(data_apartments, data_users, info)


