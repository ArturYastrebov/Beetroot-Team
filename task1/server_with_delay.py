import asyncio
import random

from task1.utils import add_reaction_to_request


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handler_message(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        ip_client, port_client = writer.get_extra_info("peername")
        print(f'Client {ip_client}:{port_client} connecting')
        while True:
            data_byte = await self.read_message(reader)
            if not data_byte:
                break
            print(f"Get message from {port_client}: {data_byte.decode('utf-8')}")
            if data_byte.decode('utf-8') == 'close_connect':
                print(f"Get close connect command")
                await asyncio.sleep(5)
                await self.close_connect(writer, port_client)
                break
            try:
                data_byte = add_reaction_to_request(data_byte.decode('utf-8'))
            except:
                print("get error format message")
            asyncio.create_task(self.write_message(data_byte, writer))


    async def read_message(self, reader):
        data_byte = await reader.read(1024)
        return data_byte

    async def write_message(self, msg_byte, writer):
        rnd = random.randint(3, 5)
        await asyncio.sleep(rnd)
        print(f'Sent message {msg_byte.decode("utf-8")} with delay {rnd}')
        writer.write(msg_byte)
        await writer.drain()

    async def start_server(self):
        print(f'Start server host {self.host}')
        server = await asyncio.start_server(self.handler_message, self.host, self.port)
        async with server:
            await server.serve_forever()

    async def close_connect(self, writer: asyncio.StreamWriter, port_client):
        print(f'connect with client {port_client} was close')
        writer.close()
        await writer.wait_closed()

async def main():
    server = Server('localhost', 8383)
    await server.start_server()

if '__main__' == __name__:
    asyncio.run(main())
