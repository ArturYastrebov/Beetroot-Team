import asyncio
import json
from dataclasses import dataclass

HOST = "localhost"
PORT = 8080

sessions_group = {}
apartments_group = {}

@dataclass
class connect_data:
    id: int
    connection: asyncio.StreamWriter
    status: str = 'ok'
    device:  str = 'client'
    # group_id: str = '201124111'

def is_json(s):
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False

# "id":"hub&&201124111",
# "data":"Apartment1&&room1&&0001&&room2&&0001&&room3&&0002%%Apartment2&&room1&&0001&&room2&&0001&&room3&&0001%%"

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    port = addr[1]
    sessions_group[port] = writer
    print(f"New connection from {addr!r}")
    while True:
        data = await reader.read(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received {message!r}")
        session_message = f"Message from {port}: {message}"
        if is_json(message):
            message = json.loads(message)
            device_id = message.get('id').split('&&')[1]
            data_apartments = [apartment for apartment in message.get('data').split('%%') if apartment]
            apartments = [apartment.split('&&') for apartment in data_apartments]
            for apartment in apartments:
                apartments_group[apartment[0]] = dict(zip(apartment[1::2], apartment[2::2]))
                session_message = f'Message from the hub_id {device_id}:'
                alarm = False
                for apartment, data in apartments_group.items():
                    for room, status in data.items():
                        if status == "0002":
                            alarm = True
                            session_message += f'\n{apartment}: {room} smoke detector alarm'
                if not alarm:
                    session_message += ' everything is ok'
        for session in sessions_group.values():
            print('session_message', session_message)
            session.write(session_message.encode())
            await session.drain()
    await writer.wait_closed()
    print(f"{port} was deleted")


async def main():
    server = await asyncio.start_server(
        handle_client, HOST, PORT)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
