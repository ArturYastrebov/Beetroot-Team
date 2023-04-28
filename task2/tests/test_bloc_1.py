import pytest
import pytest_asyncio
import asyncio
from task2.client_task2 import Client

REQ2 = '{"request_id": "02","data": "Device1&&name&&dev_name&&temperature&&15%%Device2&&name&&dev_name&&temperature&&14"}'
RESP2 = '{"request_id": "02", "data": {"Device1": {"name": "dev_name", "temperature": "15", "reaction": "Chilled Out!"}, "Device2": {"name": "dev_name", "temperature": "14", "reaction": "Chilled Out!"}}}'
REQ1 = '{"request_id": "02","data": "Device1&&name&&dev_name&&temperature&&14%%Device2&&name&&dev_name&&temperature&&13"}'
RESP1 = '{"request_id": "02", "data": {"Device1": {"name": "dev_name", "temperature": "14", "reaction": "Chilled Out!"}, "Device2": {"name": "dev_name", "temperature": "13", "reaction": "Chilled Out!"}}}'


@pytest.mark.asyncio
@pytest.mark.parametrize('req, resp', [(REQ2, RESP2), (REQ1, RESP1)])
async def test_connect_to_db(create_client, req, resp):
    await create_client.write_message(req)
    expected_result = await create_client.read_message()
    assert expected_result.decode('utf-8') == resp


@pytest.mark.asyncio
async def test_connect_to_db_param(create_client, parametrize_req):
    REQ, RESP = parametrize_req
    await create_client.write_message(REQ)
    expected_result = await create_client.read_message()
    assert expected_result.decode('utf-8') == RESP
