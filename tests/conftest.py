import asyncio
import json
from json import JSONDecodeError

import pytest

import pytest_asyncio
from TCP_server import TCPServer


# @pytest.fixture(scope="session")
# def event_loop():
#     return asyncio.get_event_loop()
#
# @pytest.fixture(scope='session')
# def server():
#     asyncio.run(TCPServer())
# server = await TCPServer()
# asyncio.run(TCPServer())
# yield server
# await server.close()


@pytest.fixture
async def client():
    reader, writer = await asyncio.open_connection("localhost", 8080)
    return reader, writer
    # yield (reader, writer)
    # writer.close()
    # await writer.wait_closed()


def check_reaction(data_file):
    try:
        data = json.loads(data_file)
        cars = data.get('data')
        for car_data in cars.values():
            speed = car_data.get('speed')
            reaction = car_data.get('reaction')
            if speed and reaction:
                try:
                    speed = int(speed)
                    if not speed <= 50 and reaction == 'Nothing' or 50 > speed >= 55 and reaction == 'Warning' or 55 > speed >= 60 and reaction == 'Warning' or 60 > speed and reaction == 'Revoddke License':
                        return False
                except TypeError:
                    raise TypeError
    except JSONDecodeError:
        raise 'JSONDecodeError'
    return True

params_data = [('{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}',
                        '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "25", "reaction": "Nothing"}, "Car2": {"speed": "35", "reaction": "Nothing"}}}'),
                        ('{"request_id": "02", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}',
                        '{"request_id": "02", "data": {"Car1": {"name": "some_name", "speed": "25", "reaction": "Nothing"}, "Car2": {"speed": "35", "reaction": "Nothing"}}}'),
                        ('{"request_id": "03", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}',
                        '{"request_id": "03", "data": {"Car1": {"name": "some_name", "speed": "25", "reaction": "Nothing"}, "Car2": {"speed": "35", "reaction": "Nothing"}}}'),
                        ('{"request_id": "04", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}',
                        '{"request_id": "04", "data": {"Car1": {"name": "some_name", "speed": "25", "reaction": "Nothing"}, "Car2": {"speed": "35", "reaction": "Nothing"}}}')]

def create_ids(data):
    return [f"request_id: {json.loads(item[0])['request_id']}" for item in data]


@pytest.fixture(params=params_data, ids=create_ids(params_data))
def params_data(request):
    return request.param


