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
        # await asyncio.sleep(5)
        if self.writer.is_closing():
            self.writer.close()
            await self.writer.wait_closed()


Response3 = '{"result": "success", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Response4 = '{"result": "success2", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Request3 = '{"request_id": "123", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'

async def main():
    client = Client('localhost', 8686)
    await client.connect_to_server()
    await client.write_message(Response3)
    await client.write_message(Response4)
    await client.read_message()
    await client.read_message()
    await client.close_connect()

if '__main__' == __name__:
    asyncio.run(main())