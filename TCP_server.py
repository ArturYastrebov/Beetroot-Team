import asyncio
import json

from config import HOST, PORT
from utils import is_json


async def reactions(car):
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


async def pasr_request(msg):
    my_dict_data = {}
    request_id = msg.get('request_id')
    data = msg.get('data')
    hendler_data = data.split('%%')
    # 'Car1&&name&&some_name&&speed&&25
    for i in hendler_data:
        if i:
            item = i.split('&&')
            cars_data = dict(zip(item[1::2], item[2::2]))
            cars_data = await reactions(cars_data)
            my_dict_data[item[0]] = cars_data
    RESP = {"request_id": request_id}
    RESP["data"] = my_dict_data
    RESP = json.dumps(RESP)
    return RESP


async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"connect client addres: {addr[0]}")
    data = await reader.read(100)
    request = data.decode()
    print(request)
    if await is_json(request):
        message = json.loads(request)
        print(f'receive message {message} from client {addr[0]}')
        response = await pasr_request(message)
    else:
        response = 'Data Error'
    print(f'send message {response} to client {addr[0]}')
    writer.write(response.encode())
    await writer.drain()


async def TCPServer():
    server = await asyncio.start_server(handle_echo, host=HOST, port=PORT)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(TCPServer())
