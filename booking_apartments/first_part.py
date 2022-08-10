import json
import re
import string
import random
import sys

path_data = 'data.users_example.json'


def greeting():
    while 1:
        user_said = input('\033[1;34mWelcome to the booking apartments\nHave you ever been here before? Yes(Y)/NO(N) or (0)Exit\033[0m ').upper()
        actions = {'Y': check_login(data_users), 'N': registration(data_users), '0': sys.exit()}
        actions[user_said] if user_said in actions else print('\033[1;31mIncorrect value, please try again:\033[0m')


def load_data_users(path_data: str) -> dict:
    with open(path_data, "r") as f:
        data_users = json.load(f)
        return data_users


path_data = 'data/users_example.json'
data_users = load_data_users(path_data)
print(data_users)

def update_data_users(path_data: str ,data_users : dict):
    with open(path_data, 'w') as f:
        json.dump(data_users, f, indent=4)


def check_login(data_users):
    while 1:
        login = input('\033[1;34mEnter your login or return(R): \033[0m')
        if login.upper() == "R": greeting()
        elif login in data_users.keys():
            while 1:
                pasword= input("\033[1;34mEnter password or return(R): \033[0m")
                if pasword.upper() == 'R': break
                elif pasword != data_users[login]["password"]:
                    print(f'\033[1;31mWrong password for login {login}, try again\033[0m')
                else:
                    print(f'\033[1;34mYou are welcome, {data_users[login]["name"]} {data_users[login]["second_name"]}\033[0m')
                    return sys.exit()
        else: print(f'\033[1;31mSorry, we dont have any users wich login is {login}\033[0m')


def input_login(data_users):
    print ('\033[1;34mHello new Usesr!\033[0m')
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
        password = input('\033[1;34mEnter the password:\033[0m')
        if (len(password) < 8 or len(password) > 20):
            print('\033[1;31mpassword must be from 8 to 20 characters long\033[0m')
        elif re.search(r'[!@#$%^&+=]',password) is None:
            print('\033[1;31mpassword must contain atleast one special symbol\033[0m')
        elif re.search(r'\d',password) is None:
            print('\033[1;31mpassword must contain atleast one digit\033[0m')
        elif re.search('[A-Z]',password) is None:
            print('\033[1;31mpassword must contain atleast one capital letter\033[0m')
        elif re.match(r'[a-z A-Z 0-9 !@#$%^&+=]{8,20}', password):
            print('\033[1;34mpassword is correct\033[0m')
            return password
        else:
            print('\033[1;31mpassword invalid\033[0m')


def generator_password():
    combination = string.ascii_letters +string.digits +string.punctuation
    password = ''
    for i in range(10):
        password += combination[random.randint(0, len(combination)-1)]
    print(f'\033[1;34mGreat! Your password is: {password}\033[0m')
    return password


def registration(data_users):
    login = input_login(data_users)
    user_said = input('\033[1;34mWould you like to generate password? yes(Y) or no(N)\033[0m').upper()
    password = ''
    while not password:
        if user_said == "Y": password = generator_password()
        elif user_said == "N": password = input_password()
        else: print('\033[4;31Incorrect value, please try again:\033[0m')
    name = input_name_or_second_name("name")
    second_name = input_name_or_second_name("second name")
    data_users[login] = {"password": password, 'name': name, "second_name": second_name, "balance": '0'}
    print(f'\033[1;34mAccount has been created!!! You are welcome, {data_users[login]["name"]} {data_users[login]["second_name"]}\033[0m')
    update_data_users(path_data, data_users)
    return sys.exit()


greeting()