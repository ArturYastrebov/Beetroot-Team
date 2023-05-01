# 1.    Inversion parsing from a response to a request format:
import json

Response = '{"result": "success", "data": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}'
Request = '{"request_id": "123", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'


def from_resp_to_req(resp: str) -> str:
    id_items = []
    for num, i in enumerate(json.loads(resp)['data'], start=1):
        str_items = f'{num}'
        for key, value in i.items():
            str_items += f'&&{key}&&{value}'
        id_items.append(str_items)
    res_dict = {"request_id": json.loads(resp)['result'], "data": '%%'.join(id_items)}
    return json.dumps(res_dict)

# print(Response)
# print(from_resp_to_req(Response))

# 2.    Inversion parsing from a request to a response format:
Request2 = '{"request_id": "123", "data": "1&&name&&Alice&&age&&30%%2&&name&&Bob&&age&&25"}'
Response2 = '{"result": "success", "data": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}'


def from_req_to_resp(req: str) -> str:
    str_data_pars = json.loads(req)['data']
    data_list = []
    for i in str_data_pars.split('%%'):
        items = i.split('&&')
        res = {'id': items[0]}
        res.update(dict(zip(items[1::2], items[2::2])))
        data_list.append(res)
    res = {'result': json.loads(req)["request_id"], 'data': data_list}
    return json.dumps(res)


# print(from_req_to_resp(Request2))

# 3.    Inversion parsing from a response to a nested dictionary:
Response3 = '{"result": "success", "data": {"user": {"id": 1, "name": "Alice", "age": 30}, "status": "active"}}'
Dictionary3 = {"user": {"id": 1, "name": "Alice", "age": 30}, "status": "active"}

def resp_to_dict(resp):
    return json.loads(resp)['data']

# print(resp_to_dict(Response3))

# 4.    Inversion parsing from a nested dictionary to a response:
Dictionary4 = {"user": {"id": 1, "name": "Alice", "age": 30}, "status": "active"}
Response4 = '{"result": "success", "data": {"user": {"id": 1, "name": "Alice", "age": 30}, "status": "active"}}'

def dict_to_rest(dict_obj: dict) -> str:
    return json.dumps({"result": "success", "data": dict_obj})

print(dict_to_rest(Dictionary4))