import itertools
import json

REQ = '{"request_id": "01", "data": "Device1&&name&&dev_name&&temperature&&25%%Device2&&name&&dev_name&&temperature&&4"}'
RESP = '{"request_id": "01", "data": {"Device1": {"name": "dev_name", "temperature": "25"},"Device2": {"name": "dev_name", "temperature": "4"}}}'


def str_like_json_to_dict(str_obj: str):
    dict_obj = json.loads(str_obj)
    return dict_obj


dict_obj = str_like_json_to_dict(RESP)
list_req = [(i, ([(x, y) for x, y in j.items()])) for i, j in dict_obj.get('data').items()]
list_res = []
for i, j in list_req:
    list_res.append(f"{i}$$${'$$$'.join(list(itertools.chain.from_iterable(j))).replace(' ', '_')}")
res_data = '%%%'.join(list_res)
req_answer = {"request_id": dict_obj["request_id"]}
req_answer.update({'data': res_data})
# print(req_answer)

def parse_response(RESP):
    my_res_list = []
    for device, data_device in json.loads(RESP)['data'].items():
        str_res = device
        for key, value in data_device.items():
            str_res += f"&&{key}&&{value}"
        my_res_list.append(str_res)
    answer = str({"request_id": json.loads(RESP)['request_id'], 'data': '%%'.join(my_res_list)})
    print(type(answer))
    return answer

print(parse_response(RESP))