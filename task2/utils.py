import json


def is_json(str_like_json):
    try:
        data_dict = json.loads(str_like_json)
        return True
    except:
        return False


def json_to_dict(json_str: str) -> dict:
    data_dict = json.loads(json_str)
    return data_dict


def dict_to_json(data_dict: dict) -> str:
    json_str = json.dumps(data_dict)
    return json_str


REQ = {"request_id": "01", "data": "Device1&&name&&dev_name&&temperature&&25%%Device2&&name&&dev_name&&temperature&&4"}
RESP = {"request_id": "01", "data": {"Device1": {"name": "dev_name", "temperature": "25", "reaction": "Hot & Sweaty!",
                                                 "Device2": {"name": "dev_name", "temperature": "4",
                                                             "reaction": "Icy Cool!"}}}}
# Сервер имитирует системы термостата умного дома и формирует фидбек по температуре в запросе
# в формате температура -> реакция:
# До 10°C включительно - Icy Cool!
# 11°C - 15°C - Chilled Out!
# 16°C - 19°C - Cool Man!
# 20°C - 22°C - Too Warm!
# Больше 22°C - Hot & Sweaty!


def pars_request(request_data: dict) -> dict:
    data = request_data['data']
    devices = data.split('%%')
    data_value = {}
    for device in devices:
        res_data = device.split("&&")
        data_value.update({res_data[0]: dict(zip(res_data[1::2], res_data[2::2]))})
    request_data.update({"data": data_value})
    return request_data


def add_reaction_to_req(request_data_dict):
    for device, data_device in request_data_dict['data'].items():
        request_data_dict['data'][device].update(analizator_reaction(int(data_device['temperature'])))
    return request_data_dict

def analizator_reaction(num: int) -> dict:
    if num <= 10:
        reaction = {"reaction": "Icy Cool!"}
    elif 11 <= num <= 15:
        reaction = {"reaction": "Chilled Out!"}
    elif 16 <= num <= 19:
        reaction = {"reaction": "Cool Man!"}
    elif 20 <= num <= 22:
        reaction = {"reaction": "Too Warm!"}
    elif 22 < num:
        reaction = {"reaction": "Hot & Sweaty!"}
    return reaction


def create_response_with_react(req: str) -> str:
    req_dict = json_to_dict(req)
    dict_req_with_pars = (pars_request(req_dict))
    dict_response = add_reaction_to_req(dict_req_with_pars)
    str_response = dict_to_json(dict_response)
    return str_response
