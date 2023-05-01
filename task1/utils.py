import asyncio
import json

REQ = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}'


def parser(REQ) -> dict:
    REQ_dict = json.loads(REQ)
    res_dict = {"request_id": REQ_dict["request_id"]}
    data = REQ_dict["data"].split('%%')
    data_dict = {}
    for item in data:
        if item:
            car = item.split('&&')
            data_dict.update({car[0]: dict(zip(car[1::2], car[2::2]))})
    res_dict.update({'data': data_dict})
    print(res_dict)
    return res_dict


# Сервер имитирует реакцию системы контроля скорости и имеет следующие характеристики:
# • Если вы едете со скоростью 50 км/ч или меньше, ничего не произойдет.(Reaction - Nothing)
# • Если вы едете со скоростью более 50 км/ч, но не более 55 км/ч, вы получите предупреждение.(Warning)
# • Если вы едете со скоростью более 55 км/ч, но не более 60 км/ч, вы будете оштрафованы.(Penalty)
# • Если вы едете со скоростью более 60 км/ч, действие ваших водительских прав будет приостановлено.(Revoke License)
# • Скорость в км/ч доступна системе как целочисленное значение.
def add_reaction(req_dict):
    for car, car_data in req_dict.get('data').items():
        req_dict['data'][car].update(check_reaction(int(car_data.get('speed'))))
    return req_dict

def check_reaction(speed: int) -> dict:
    if speed <= 50:
        reaction = 'Nothing'
    elif 55 >= speed > 50:
        reaction = 'Warning'
    elif 60 >= speed > 55:
        reaction = 'Penalty'
    elif speed > 60:
        reaction = 'Revoke License'
    return {'reaction': reaction}


def add_reaction_to_request(str_json):
    req_dict = parser(str_json)
    resp_dict_with_reaction = add_reaction(req_dict)
    resp_str_json = json.dumps(resp_dict_with_reaction)
    return resp_str_json.encode('utf-8')

