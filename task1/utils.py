# Inversion parsing from a response to a request format:
import json




def is_json(str_like_json):
    try:
        data = json.loads(str_like_json)
        return True
    except json.JSONDecodeError:
        return False


def req_to_res(resp):
    data = json.loads(resp)['data']
    data_list_res = []
    for device, data_device in data.items():
        str_data = device
        for key, value in data_device.items():
            str_data += f'&&{key}&&{value}'
        data_list_res.append(str_data)
    res_dict = {"request_id": json.loads(resp)["request_id"], "data": '%%'.join(data_list_res)}
    return json.dumps(res_dict)


