import asyncio
import json
from json import JSONDecodeError

import pytest

import pytest_asyncio
from tcp_test.TCP_server import TCPServer


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
                except Exception:
                    raise '1111111111111111'
    except JSONDecodeError:
        raise ('JSONDecodeError')
    return True

@pytest.fixture(params=['{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&60%%Car2&&speed&&35%%"}',
                         '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&50%%Car2&&speed&&25%%"}',
                         '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&60%%Car2&&speed&&35%%"}',
                         '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&50%%Car2&&speed&&25%%"}',
                         '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&40%%Car2&&speed&&70%%"}',
                         '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&50%%Car2&&speed&&100%%"}'])
def test_parametrized_data(request):
    return request.param
