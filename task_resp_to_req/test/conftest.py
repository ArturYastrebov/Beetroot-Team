import pytest
import pytest_asyncio
import asyncio

from task_resp_to_req.client import Client

@pytest_asyncio.fixture()
async def client():
    client = Client('localhost', 8686)
    await client.connect_to_server()
    yield client
    await client.close_connect()


Response3 = '{"result": "success3", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Response4 = '{"result": "success4", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Request3 = '{"request_id": "success3", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'
Request4 = '{"request_id": "success4", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'

@pytest_asyncio.fixture(params=[(Response3, Request3), (Response4, Request4)], ids=['req3', 'req4'])
async def parametrize_req(request):
    return request.param