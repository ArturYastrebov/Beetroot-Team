import json
async def is_json(s):
    try:
        json.loads(s)
        return True
    except:
        return False


# {'request_id': '01', 'data': 'Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%'}

# RESP =
# {
# 'request_id': '01',
# 'data': {
# 'Car1': {'name': 'some_name',
# 'speed': '25', reaction: "Nothing"},
# 'Car2': {'speed', '35', reaction: "Nothing"}
# }
def check_data(cars_data):
    #     {"Car1": {"name": "some_name", "speed": "25", "reaction": "Nothing"}, "Car2": {"speed": "35", "reaction": "Nothing"}}
    if isinstance(cars_data, dict):
        for car in cars_data.values():
            if isinstance(car, dict):
                num = car.get("speed")
                try:
                    num = int(num)
                except:
                    raise ValueError
    else:
        raise ValueError