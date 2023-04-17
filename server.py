import asyncio
import dataclasses
import json

from config import HOST, PORT
from utils import is_json


@dataclasses.dataclass
class Connect:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter


class TCPAsyncServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.connect = Connect

    async def handle_client(self, reader, writer):
        self.connect = Connect(reader=reader, writer=writer)
        server_addres = writer.get_extra_info('peername')
        print(f"connect client addres: {server_addres}")
        data = await reader.read(100)
        request = data.decode()
        print(request)
        if await is_json(request):
            message = json.loads(request)
            print(f'receive message {message} from client {server_addres}')
            response = await self.pasr_request(message)
        else:
            response = 'Data Error'
        print(f'send message {response} to client {server_addres}')
        writer.write(response.encode())
        await writer.drain()

    async def pasr_request(self, msg):
        my_dict_data = {}
        request_id = msg.get('request_id')
        data = msg.get('data')
        hendler_data = data.split('%%')
        # 'Car1&&name&&some_name&&speed&&25
        for i in hendler_data:
            if i:
                item = i.split('&&')
                cars_data = dict(zip(item[1::2], item[2::2]))
                cars_data = await self.reactions(cars_data)
                my_dict_data[item[0]] = cars_data
        RESP = {"request_id": request_id}
        RESP["data"] = my_dict_data
        RESP = json.dumps(RESP)
        return RESP

    async def reactions(self, car):
        speed = int(car.get('speed'))
        if speed:
            if speed <= 50:
                car['reaction'] = 'Nothing'
            elif 50 > speed >= 55:
                car['reaction'] = 'Warning'
            elif 55 > speed >= 60:
                car['reaction'] = 'Penalty'
            elif 60 > speed:
                car['reaction'] = 'Revoke License'
        return car

    async def start(self):
        self.server = await asyncio.start_server(
            self.handle_client, self.host, self.port)
        async with self.server:
            await self.server.serve_forever()

    async def stop(self):
        if self.server:
            self.server.close()

    async def wait_closed(self):
        if self.server:
            await self.server.wait_closed()


server = TCPAsyncServer(HOST, PORT)


async def main():
    await server.start()


if __name__ == '__main__':
    asyncio.run(main())


