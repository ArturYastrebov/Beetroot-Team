import asyncio

from task2.client_task2 import Client

DB_REQ = '{"request_id": "01", "data": "db_connect"}'
DB_RESP = '{"request_id": "01", "data": "db_connected"}'

async def main():
    client = Client('localhost', 8484)
    await client.connect_to_server()
    await client.connect_to_db()
    REQ ='{"request_id": "02","data": "Device1&&name&&dev_name&&temperature&&15%%Device2&&name&&dev_name&&temperature&&14"}'
    REQ2 ='{"request_id": "03","data": "Device1&&name&&dev_name&&temperature&&55%%Device2&&name&&dev_name&&temperature&&24"}'
    REQ3 ='{"request_id": "04","data": "Device1&&name&&dev_name&&temperature&&5%%Device2&&name&&dev_name&&temperature&&4"}'
    await client.write_message(REQ)
    # await client.write_message(REQ2)
    # await client.write_message(REQ3)
    # await client.read_message()
    # await client.read_message()
    await client.read_message()
    await client.close_db_connect()
    await client.close_connect()

if '__main__' == __name__:
    asyncio.run(main())
