import json


def parse_data_form_json_file(filename: str) -> list:
    with open(filename, "r") as f:
        data_users = json.load(f)
    return data_users


def save_data_to_json_file(filename: str, data) -> str:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    return filename

INPUT_USERS: str = 'resources/users.json'
OUTPUT_USERS: str = 'resources/users.json'
INPUT_APARTMENTS: str = 'resources/apartments.json'
OUTPUT_APARTMENTS: str = 'resources/apartments.json'