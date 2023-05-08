import asyncio
import random

from task1.utils import is_json, req_to_res


class Server_TCP:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handler_message(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        ip_client, port_client = writer.get_extra_info('peername')
        print(f'client {ip_client}:{port_client} connect to server')
        while True:
            msg_byte = await self.read_message(reader)
            msg_str = msg_byte.decode('utf-8')
            if not msg_byte:
                continue
            elif 'Close_connect' in msg_str and not writer.is_closing():
                print('connect was closet')
                writer.close()
                await writer.wait_closed()
                break
            elif is_json(msg_str):
                req = req_to_res(msg_str)
                msg_byte = req.encode('utf-8')
            asyncio.create_task(self.write_message(writer, msg_byte))

    async def read_message(self, reader: asyncio.StreamReader):
        data_byte = await reader.read(1024)
        if data_byte:
            data_str = data_byte.decode('utf-8')
            print(f"get message: {data_str}")
        return data_byte

    async def write_message(self, writer: asyncio.StreamWriter, msg_byte):
        if msg_byte == 'Close_connect'.encode('utf-8'):
            rnd = 0.2
        else:
            rnd = random.randint(1, 5)
        await asyncio.sleep(rnd)
        print(f'Server sent message {msg_byte.decode("utf-8")} with delay {rnd}')
        writer.write(msg_byte)
        await writer.drain()

    async def start_server(self):
        print('start server')
        server = await asyncio.start_server(self.handler_message, self.host, self.port)
        async with server:
            await server.serve_forever()


async def main():
    server = Server_TCP('localhost', 8181)
    await server.start_server()

if '__main__' == __name__:
    asyncio.run(main())