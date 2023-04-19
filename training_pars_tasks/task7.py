# 7.
# Task: Write a Python program to parse a TCP response from a custom protocol
# and extract specific data fields, such as username, email, and age, and store it in a JSON format.
# Example TCP response:
#
import json

data = "RESPONSE|username:john.doe|email:john.doe@example.com|age:30|status:active|"

def pars_tcp_response(data):
    response_items = data.split('|')
    contact_info = dict(key_value.split(':')for key_value in response_items[1::] if key_value)
    return {response_items[0]: contact_info}

def dict_to_json(dict_obj):
    return json.dumps(dict_obj)


dict_response = pars_tcp_response(data)
json_str_response = dict_to_json(dict_response)
print(json_str_response)


