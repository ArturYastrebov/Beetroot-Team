# 8. Like 7

import json

data = "RESPONSE;HEADER;employee_id=1234;employee_name=John Smith;job_title=Software Engineer;job_title=Data Scientist;job_title=UX Designer;"

def pars_tcp_response(data):
    response_items = data.split(';')
    contact_info = dict(key_value.split('=')for key_value in response_items[2::] if key_value)
    return {response_items[0]: {response_items[1]: contact_info}}

def dict_to_json(dict_obj):
    return json.dumps(dict_obj)


dict_response = pars_tcp_response(data)
json_str_response = dict_to_json(dict_response)
print(json_str_response)