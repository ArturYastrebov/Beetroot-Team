import json
import datetime
from pprint import pprint


def load_data_apartments(path_data: str) -> dict:
    with open(path_data, "r") as f:
        data_apartments = json.load(f)
        return data_apartments

def convert_time_to_str(date):
  return date.strftime("%d.%m.%Y")

def convert_str_to_time(data_str):
  return datetime.datetime.strptime(data_str, "%d.%m.%Y").date()

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

data_path_apartments = "data/apartments_example.json"
data_apartments = load_data_apartments(data_path_apartments)




def input_search_data():
    check_data = False
    while not check_data:
        print('\033[1;34mUser,chose the date of booking:\033[0m')
        start_date_booking, check_data = input_date()
        actions = input('\033[1;34mWould you like put down count of day - (D) or the last day of booking - (L) \033[0m')
        if actions.upper() == 'D':
            count_day = input('\033[1;34mPut count of days: \033[0m')
            end_date_booking = start_date_booking + datetime.timedelta(int(count_day))
        elif actions.upper() == 'L':
            print('\033[1;34mUser,chose the last date of booking:\033[0m')
            end_date_booking, check_data = input_date()
        else:
            print('\033[31mIncorrect value, please try again\033[0m')
            return input_search_data()
        if start_date_booking > end_date_booking:
            check_data = False
            print('\033[31mOMG!!! start_date_booking > end_date_booking, try again.\033[0m')
    return start_date_booking, end_date_booking


def collect_input_inf():
    count_of_people = input_count_of_people()
    max_money = input_count_of_max_money()
    start_date_booking, end_date_booking = input_search_data()
    return show_apartment(data_apartments, start_date_booking, end_date_booking, count_of_people, max_money)


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

def show_apartment(data_apartments, start_date_booking, end_date_booking, count_of_people, max_money):
    print(f'In your days >>> {convert_time_to_str(start_date_booking)} - {convert_time_to_str(end_date_booking)} <<< available:')
    count = 0
    key_id = {}
    for key, apartment in data_apartments.items():
        if count_of_people <= int(apartment["people"]):
            if max_money >= int(apartment["price"]):
                for period_time in apartment['free_time']:
                    if convert_str_to_time(period_time[0]) <= start_date_booking and (
                            end_date_booking <= convert_str_to_time(period_time[1])):
                        count += 1
                        print(f'\n\033[1;7m*** {key} ***\033[0m\nUp to {apartment["people"]} people can live in the apartments\nPrice per day: {apartment["price"]}')
                        print(f'Description : {apartment["description"]}\n\033[1;34m>>>> {count} <<<< press, if you want to book {key} <<<\033[0m')
                        key_id[str(count)] = key
    return choice_num_apart(key_id, start_date_booking, end_date_booking)


def choice_num_apart(key_id, start_date_booking, end_date_booking):
    while 1:
        actions = input(f"\n_________________________________\n\033[1;34mPut down from 1 to {len(key_id)} or Return (R)\033[0m")
        if actions.upper() == "R":
            collect_input_inf()
        elif actions.isdigit():
            if int(actions) in list(range(1, len(key_id)+1)):
                apart = key_id[actions]
                print(apart)
                return booking_apartment(data_apartments, apart, start_date_booking, end_date_booking)
        print('\033[31mIncorrect value, please try again\033[0m')


def booking_apartment(data_apartments, apart, start_date_booking, end_date_booking):
    free_time_zones = data_apartments[apart]["free_time"]
    for i, period_time in enumerate(free_time_zones):
        if (convert_str_to_time(period_time[0])) <= start_date_booking and (
                end_date_booking <= convert_str_to_time(period_time[1])):
            free_time_zones.append([period_time[0], convert_time_to_str(start_date_booking)])
            free_time_zones.append([convert_time_to_str(end_date_booking), period_time[1]])
            free_time_zones.pop(i)
            pprint(data_apartments)
            collect_input_inf()

collect_input_inf()