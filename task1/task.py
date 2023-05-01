import asyncio

from task1.client_1 import Client

REQ = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&35%%Car2&&speed&&51%%"}'

async def main():
    client = Client('localhost', 8383)
    await client.create_connect()
    await client.sent_message(REQ)
    data = await client.read_message_one_times()
    print(data)
    await client.sent_message('close_connect')


if "__main__" == __name__:
    asyncio.run(main())
