# Inversion parsing from a response to a request format:
import json

Response3 = '{"result": "success", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Request3 = '{"request_id": "123", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'


def is_json(str_like_json):
    try:
        data = json.loads(str_like_json)
        return True
    except json.JSONDecodeError:
        return False


def resp_to_req3(resp):
    res_list = []
    for num, items in enumerate(json.loads(resp)["data"]["users"], start=1):
        res_str_items = str(num)
        for key, value in items.items():
            res_str_items += f'&&{key}&&{value}'
        res_list.append(res_str_items)
    return json.dumps({"request_id": json.loads(resp)["result"], "data": '%%'.join(res_list)})

# print(resp_to_req3(Response3))