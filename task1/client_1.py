import asyncio


class Client:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.reader: asyncio.StreamReader = None
        self.writer: asyncio.StreamWriter = None

    async def sent_message(self, msg):
        print(f'sent message {msg}')
        msg_byte = msg.encode('utf-8')
        self.writer.write(msg_byte)
        await self.writer.drain()
        if 'close_connect' in msg:
            await asyncio.sleep(5)
            await self.close_connect()
        await asyncio.sleep(0.2)

    async def read_message_one_times(self):
        data_byte = await self.reader.read(1024)
        if data_byte:
            return data_byte.decode('utf-8')

    async def read_message_always(self):
        asyncio.create_task(self._read_message())

    async def _read_message(self):
        while True:
            data_byte = await self.reader.read(1024)
            if data_byte:
                print(data_byte.decode('utf-8'))


    async def create_connect(self):
        print(f'connect to server {self.host}:{self.port}')
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

    async def close_connect(self):
        if not self.writer.is_closing():
            print('close connect')
            self.writer.close()
            self.writer.is_closing()
            await self.writer.wait_closed()




async def main():
    client = Client('localhost', 8383)
    await client.create_connect()
    await client.sent_message('Hello')
    await client.sent_message('my')
    await client.sent_message('friend')
    # await asyncio.sleep(5)
    await client.sent_message('close_connect')


if "__main__" == __name__:
    asyncio.run(main())
