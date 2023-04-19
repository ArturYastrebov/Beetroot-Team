# 8. Like 7

import json

data = "RESPONSE%HEADER%user_id=1234%username=johndoe%permissions=view|edit|delete|"

def pars_tcp_response(data):
    response_items = data.split('%')
    pars_info = list(key_value.split('=')for key_value in response_items[2::] if key_value)
    contact_info = dict((key, value) if '|' not in value else (key, [i for i in value.split('|') if i]) for key, value in pars_info)
    return {response_items[0]: {response_items[1]: contact_info}}

def dict_to_json(dict_obj):
    return json.dumps(dict_obj)


dict_response = pars_tcp_response(data)
print(dict_response)
json_str_response = dict_to_json(dict_response)
print(json_str_response)