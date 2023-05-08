import asyncio


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reader: asyncio.StreamReader = None
        self.writer: asyncio.StreamWriter = None

    async def connect_to_server(self):
        print(f'connect to server {self.host, self.port}')
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)


    async def read_message(self):
        msg_byte = await self.reader.read(1024)
        msg_str = msg_byte.decode('utf-8')
        print(f'get message: {msg_str}')
        return msg_byte

    async def write_message(self, msg_str: str):
        await asyncio.sleep(0.2)
        msg_byte = msg_str.encode('utf-8')
        print(f'sent message: {msg_str}')
        self.writer.write(msg_byte)
        await self.writer.drain()

    async def close_connect(self):
        print('close connect')
        await self.write_message('Close_connect')
        if self.writer.is_closing():
            self.writer.close()
            await self.writer.wait_closed()


REQ1 = '{"request_id": "01", "data": {"Hub1": {"name": "qwe1", "id": "123"}, "Device1": {"name": "wqe1", "id": "23"}}}'
REQ2 = '{"request_id": "02", "data": {"Hub2": {"name": "qwe2", "id": "1235"}, "Device2": {"name": "wqe2", "id": "234"}}}'


async def main():
    client = Client('localhost', 8181)
    await client.connect_to_server()
    await client.write_message(REQ1)
    await client.write_message(REQ2)
    await client.read_message()
    await client.read_message()
    await client.close_connect()

if '__main__' == __name__:
    asyncio.run(main())