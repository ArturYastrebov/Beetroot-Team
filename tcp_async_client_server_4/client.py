import asyncio


class Client:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.reader: asyncio.StreamReader = None
        self.writer: asyncio.StreamWriter = None

    async def sent_msg(self, msg):
        print(f'sent message {msg}')
        msg_byte = msg.encode('utf-8')
        self.writer.write(msg_byte)
        await self.writer.drain()

    async def read_msg(self):
        while True:
            data_byte = await self.reader.read(1024)
            if data_byte:
                print(data_byte.decode('utf-8'))

    async def connect_to_server(self):
        print(f'connect to server {self.host}:{self.port}')
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        asyncio.create_task(self.read_msg())

    async def disconnect_from_server(self):
        try:
            await asyncio.sleep(10)
            await self.sent_msg('close_connect')
        except ConnectionError:
            raise ConnectionError
        finally:
            print('close connect')
            self.writer.close()
            await self.writer.wait_closed()

    async def __aenter__(self):
        await self.connect_to_server()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect_from_server()


async def main():
    async with Client('localhost', 8181) as client:
        await client.sent_msg('hello')
    # client = Client('localhost', 8181)
    # await client.connect_to_server()
    # await client.sent_msg('hello')


if "__main__" == __name__:
    asyncio.run(main())
