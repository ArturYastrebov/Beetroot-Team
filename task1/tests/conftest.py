import asyncio
import pytest
import pytest_asyncio
from task1.client_1 import Client


@pytest_asyncio.fixture()
async def client():
    client = Client('localhost', 8383)
    await client.create_connect()
    yield client
    await asyncio.sleep(5)
    await client.close_connect()


REQ1 = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&15%%Car2&&speed&&20%%"}'
RESP1 = '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "15", "reaction": "Nothing"}, "Car2": {"speed": "20", "reaction": "Nothing"}}}'
REQ2 = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&45%%Car2&&speed&&50%%"}'
RESP2 = '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "45", "reaction": "Nothing"}, "Car2": {"speed": "50", "reaction": "Nothing"}}}'
REQ3 = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&35%%Car2&&speed&&51%%"}'
RESP3 = '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "35", "reaction": "Nothing"}, "Car2": {"speed": "51", "reaction": "Warning"}}}'


@pytest_asyncio.fixture(params=[(REQ1, RESP1), (REQ2, RESP2), (REQ3, RESP3)])
async def parametrize_fixture(request):
    return request.param
