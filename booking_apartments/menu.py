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
        print('You have selected a date in the past,try again')
    except Exception:
        print('Incorrect format data,try again')
    else:
        print('Correct format data')
        return True


def input_date():
    check_data = False
    while not check_data:
        date_booking = f'{input("day")}.{input("month")}.{input("Year")}'
        check_data = check_str_data(date_booking)
    date_booking = convert_str_to_time(date_booking)
    return date_booking, check_data

data_path_apartments = "data/apartments_example.json"
data_apartments = load_data_apartments(data_path_apartments)




def input_search_data():
    check_data = False
    while not check_data:
        print('User,chose the date of booking:')
        start_date_booking, check_data = input_date()
        actions = input('Would you like put down count of day - (D) or the last day of booking - (L)')
        if actions.upper() == 'D':
            count_day = input('Put count of days')
            end_date_booking = start_date_booking + datetime.timedelta(int(count_day))
        elif actions.upper() == 'L':
            print('User,chose the last date of booking:')
            end_date_booking, check_data = input_date()
        else:
            print('Incorrect value, please try again')
            return input_search_data()
        if start_date_booking > end_date_booking:
            check_data = False
            print('OMG!!! start_date_booking > end_date_booking, try again.')
    return show_apartment(data_apartments, start_date_booking, end_date_booking)


def show_apartment(data_apartments, start_date_booking, end_date_booking):
    print(f'In your days >>> {convert_time_to_str(start_date_booking)} - {convert_time_to_str(end_date_booking)} <<< available:')
    count = 0
    key_id = {}
    for key, apartment in data_apartments.items():
        count += 1
        for i, period_time in enumerate(apartment['free_time']):
            if convert_str_to_time(period_time[0]) <= start_date_booking and (
                    end_date_booking <= convert_str_to_time(period_time[1])):
                print(f'\n*** {key} ***\nUp to {apartment["people"]} people can live in the apartments\nPrice per day: {apartment["price"]}')
                print(f'Description : {apartment["description"]}\n>>>> {count} <<<< press, if you want to book {key} <<<')
                key_id[str(count)] = key
    return choice_num_apart(key_id, start_date_booking, end_date_booking)


def choice_num_apart(key_id, start_date_booking, end_date_booking):
    while 1:
        actions = input(f"\n_________________________________\nPut down from 1 to {len(key_id)} or Return (R)")
        if actions.upper() == "R":
            print('tyt byde function')
        elif actions.isdigit():
            if int(actions) in list(range(1, len(key_id)+1)):
                apart = key_id[actions]
                print(apart)
                return booking_apartment(data_apartments, apart, start_date_booking, end_date_booking)
        print('Incorrect value, please try again')


def booking_apartment(data_apartments, apart, start_date_booking, end_date_booking):
    free_time_zones = data_apartments[apart]["free_time"]
    for i, period_time in enumerate(free_time_zones):
        if (convert_str_to_time(period_time[0])) <= start_date_booking and (
                end_date_booking <= convert_str_to_time(period_time[1])):
            free_time_zones.append([period_time[0], convert_time_to_str(start_date_booking)])
            free_time_zones.append([convert_time_to_str(end_date_booking), period_time[1]])
            free_time_zones.pop(i)
            pprint(data_apartments)
            break

input_search_data()