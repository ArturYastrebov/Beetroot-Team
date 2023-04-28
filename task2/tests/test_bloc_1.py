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
async def test_sent_req_param(client, req, resp):
    await client.write_message(req)
    expected_result = await client.read_message()
    assert expected_result.decode('utf-8') == resp


@pytest.mark.asyncio
async def test_sent_req_param_fixture(client, parametrize_req):
    REQ, RESP = parametrize_req
    await client.write_message(REQ)
    expected_result = await client.read_message()
    assert expected_result.decode('utf-8') == RESP

@pytest.mark.asyncio
async def test_connect_db(client):
    await client.write_message('REQ')
    RESP = await client.read_message()
    assert RESP.decode('utf-8') == 'REQ'

