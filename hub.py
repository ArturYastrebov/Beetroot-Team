import asyncio
import json
import random

HOST = "localhost"
PORT = 8080


async def write_message(writer: asyncio.StreamWriter, data: bytes):
    writer.write(data)
    await writer.drain()


async def listen(reader: asyncio.StreamReader):
    print("Listening...")
    while True:
        print("Waiting for message...")
        data = await reader.read(1024)
        message = data.decode()
        if not message:
            raise Exception("Connection closed")
        print(f"Received {message!r}")


async def enter_messages(writer: asyncio.StreamWriter):
    for _ in range(1, 10):
        await asyncio.sleep(2)
        REQ = {
            "id": "hub&&201124111",
            "data": f"Apartment1&&room1&&0001&&room2&&000{random.randint(1, 3)}&&room3&&0001%%"
                    f"Apartment2&&room1&&000{random.randint(1, 3)}&&room2&&{random.randint(1, 3)}&&room3&&0001%%"}
        message = json.dumps(REQ)
        await write_message(writer, message.encode("utf-8"))
        print(f"Sent {message!r}")


async def start_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    await asyncio.gather(listen(reader), enter_messages(writer))


asyncio.run(start_client())
