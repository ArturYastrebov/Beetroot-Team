import pytest
import pytest_asyncio

@pytest.mark.asyncio
@pytest.mark.parametrize('message, expected',[
                         ("hello", "hello"),
                         ('111', '111')
                         ])
async def test_echo_successful(client, message, expected):
    await client.sent_message(message)
    answer = await client.get_answer()
    assert answer == expected

@pytest.mark.asyncio
async def test_echo_successful2(client, param_fixture):
    message, expected = param_fixture
    await client.sent_message(message)
    answer = await client.get_answer()
    assert answer == expected
