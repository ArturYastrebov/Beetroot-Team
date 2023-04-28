import pytest
import pytest_asyncio
import asyncio
from task2.client_task2 import Client
@pytest_asyncio.fixture()
async def create_client():
    client = Client('localhost', 8484)
    await client.connect_to_server()
    yield client
    await client.close_connect()

REQ3 = '{"request_id": "03","data": "Device1&&name&&dev_name&&temperature&&55%%Device2&&name&&dev_name&&temperature&&24"}'
RESP3 = '{"request_id": "03", "data": {"Device1": {"name": "dev_name", "temperature": "55", "reaction": "Hot & Sweaty!"}, "Device2": {"name": "dev_name", "temperature": "24", "reaction": "Hot & Sweaty!"}}}'
REQ4 = '{"request_id": "04","data": "Device1&&name&&dev_name&&temperature&&5%%Device2&&name&&dev_name&&temperature&&4"}'
RESP4 = '{"request_id": "04", "data": {"Device1": {"name": "dev_name", "temperature": "5", "reaction": "Icy Cool!"}, "Device2": {"name": "dev_name", "temperature": "4", "reaction": "Icy Cool!"}}}'

@pytest_asyncio.fixture(params=[(REQ3, RESP3),(REQ4, RESP4)], ids=['req3','req4'])
async def parametrize_req(request):
    return request.param
