# Inversion parsing from a response to a request format:
import json

Response = '{"result": "success", "data": {"id": 1, "name": "Alice", "age": 30, "address": {"street": "123 Main St", "city": "New York", "state": "NY"}}}'
Request = '{"request_id": "123", "data": "1&&id&&1&&name&&Alice&&age&&30&&address&&street&&123 Main St&&address&&city&&New York&&address&&state&&NY"}'
def resp_to_req(resp):
    str_res = '1'
    for key, value in json.loads(resp)["data"].items():
        if isinstance(value, dict):
            str_dict = f'&&{key}'
            for key2, value2 in value.items():
                str_dict += f'&&{key2}&&{value2}'
        else:
            str_res += f'&&{key}&&{value}'
    return json.dumps({"request_id": json.loads(resp)["result"], "data": str_res+str_dict})


# print(resp_to_req(Response))


# Inversion parsing from a response to a request format:
Response2 = '{"result": "success", "data": [{"id": 1, "name": "Alice", "age": 30, "address": {"street": "123 Main St", "city": "New York", "state": "NY"}}, {"id": 2, "name": "Bob", "age": 25, "address": {"street": "456 Elm St", "city": "San Francisco", "state": "CA"}}]}'
Request2 = '{"request_id": "123", "data": "1&&id&&1&&name&&Alice&&age&&30&&address&&street&&123 Main St&&address&&city&&New York&&address&&state&&NY%%2&&id&&2&&name&&Bob&&age&&25&&address&&street&&456 Elm St&&address&&city&&San Francisco&&address&&state&&CA"}'


def resp_to_req2(resp):
    data_list_items = []
    for num, items in enumerate(json.loads(resp)["data"], start=1):
        str_answer = str(num)
        for key, value in items.items():
            if isinstance(value, dict):
                str_res_items = f'&&{key}'
                for key2, value2 in value.items():
                    str_res_items += f'&&{key2}&&{value2}'
            else:
                str_answer += f'&&{key}&&{value}'
        data_list_items.append(str_answer+str_res_items)
    return json.dumps({'request_id': json.loads(resp)["result"], 'data': '%%'.join(data_list_items)})


# print(resp_to_req2(Response2))

# Inversion parsing from a response to a request format:
Response3 = '{"result": "success", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Request3 = '{"request_id": "123", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'


def resp_to_req3(resp):
    res_list = []
    for num, items in enumerate(json.loads(resp)["data"]["users"], start=1):
        res_str_items = str(num)
        print(num)
        print(items)
        for key, value in items.items():
            res_str_items += f'&&{key}&&{value}'
        res_list.append(res_str_items)
    return json.dumps({"request_id": json.loads(resp)["result"], "data": '%%'.join(res_list)})

print(resp_to_req3(Response3))


