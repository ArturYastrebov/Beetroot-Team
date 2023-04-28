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

    async def connect_to_db(self):
        await self.write_message('connect to DB')
        await self.read_message()


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
        self.writer.close()
        await self.writer.wait_closed()


async def main():
    client = Client('localhost', 8484)
    await client.connect_to_server()
    await client.connect_to_db()
    await client.write_message('hello')
    await client.write_message('my')
    await client.write_message('friend')
    await client.read_message()
    await client.read_message()
    await client.read_message()
    await client.close_connect()

if '__main__' == __name__:
    asyncio.run(main())

