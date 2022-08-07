

def main_menu(list_of_apt: dict):
    print('\033[1;34mWhat do you want to do?\033[0m')
    selection = {'1': booking_apartments, '2': add_apartments, '3': update_balance, '0': greetings}
    user_said = input('\033[1;32m1 - Start booking\n'
                      '2 - Submit apartment to offer\n'
                      '3 - Update your balance\033[0m\n'
                      '\033[37m0 - Quit from menu\033[0m\n')
    selection[user_said](list_of_apt) if user_said in selection \
        else print('\033[4;31Incorrect value, please try again:\033[0m'),\
        main_menu(list_of_apt)

def booking_apartments():
    print('booking')

def add_apartments():
    print('add')

def update_balance():
    print('update')

def greetings():
    print('Greetings')

main_menu(list_of_apt=0)