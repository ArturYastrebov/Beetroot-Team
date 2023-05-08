import asyncio
import random


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.session = {}

    async def handler_msg(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        ip_client, port_client = writer.get_extra_info('peername')
        self.session[port_client] = writer
        print(f'Connect client addr:{ip_client}:{port_client}')
        while True:
            msg_byte = await self.read_msg(reader, port_client)
            if not msg_byte:
                break
            elif msg_byte.decode('utf-8') == 'close_connect':
                await self.close_connections(writer, port_client)
                break
            asyncio.create_task(self.write_answer(msg_byte, port_client))

    async def read_msg(self, reader: asyncio.StreamReader, port_client):
        msg_byte = await reader.read(1024)
        print(f'get message from {port_client}: {msg_byte.decode("utf-8")}')
        return msg_byte

    async def write_answer(self, message_byte: bytes, port_client):
        rnd = random.randint(1, 10)
        await asyncio.sleep(rnd)
        print(f"sent message from {port_client}: {message_byte.decode('utf-8')}")
        response = f"sent message with delay {rnd} sec from {port_client}: ".encode('utf-8') + message_byte
        for writer in self.session.values():
            writer.write(response)
            await writer.drain()

    async def close_connections(self, writer: asyncio.StreamWriter, port_client):
        print(f'close connections with client {port_client}')
        self.session.pop(port_client)
        writer.close()
        await writer.wait_closed()

    async def start_server(self):
        print(f'start server')
        server = await asyncio.start_server(self.handler_msg, self.host, self.port)
        async with server:
            await server.serve_forever()


async def main():
    server = Server('localhost', 8484)
    await server.start_server()


if "__main__" == __name__:
    asyncio.run(main())
