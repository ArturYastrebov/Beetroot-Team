import asyncio

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.session = {}

    async def handler_message(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        ip_client, port_client = writer.get_extra_info("peername")
        self.session[port_client] = writer
        print(f'Client {ip_client}:{port_client} connecting')
        while True:
            data_byte = await self.read_message(reader, port_client)
            if not data_byte:
                break
            elif data_byte.decode('utf-8') == 'close_connect':
                await self.close_client_connect(writer, port_client)
                break
            asyncio.create_task(self.write_message(data_byte))

    async def read_message(self, reader, port_client):
        data_byte = await reader.read(1024)
        print(f"Get message from {port_client}: {data_byte.decode('utf-8')}")
        return data_byte

    async def write_message(self, msg_byte):
        print(f'Sent message {msg_byte}')
        for writer in self.session.values():
            writer.write(msg_byte)
            await writer.drain()

    async def start_server(self):
        print(f'Start server host {self.host}')
        server = await asyncio.start_server(self.handler_message, self.host, self.port)
        async with server:
            await server.serve_forever()

    async def close_client_connect(self, writer: asyncio.StreamWriter, port_client):
        print(f'connect with client {port_client} was close')
        self.session.pop(port_client)
        writer.close()
        await writer.wait_closed()


async def main():
    server = Server('localhost', 8181)
    await server.start_server()

if '__main__' == __name__:
    asyncio.run(main())
