import pytest_asyncio

from client import TCPAsyncClient
from config import HOST, PORT

@pytest_asyncio.fixture()
async def client():
    client = TCPAsyncClient(HOST, PORT)
    await client.open_connection()
    yield client
    client.disconnect()
    await client.wait_closed()

@pytest_asyncio.fixture(params=[
        '{"request_i": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}',
        '{"request_id": "01", "data": "Car1&&name&&some_name&&spe&35%%"}',
        '{"request_id": "&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}'
])
async def create_invalid_json_data(request):
    return request.param

@pytest_asyncio.fixture(params=[
        '{"Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}',
        '{123}',
        '{"request_id',
        '{"reque',
        '_id'
])
async def create_not_json_data(request):
    return request.param



