import asyncio
import os
import sys


IP = '192.168.0.10'
PORT = 5000


async def print_data(reader, writer):
    try:
        while True:
            try:
                byte_data = await reader.readuntil(bytes.fromhex('ee03'))
                print(f'received: {byte_data.hex()} from {writer.get_extra_info("peername")}')
            except asyncio.IncompleteReadError as e:
                pass
    except KeyboardInterrupt:
        print('callback sttoped')
        os.system('Pause')
        # sys.exit()
    except Exception as e:
        print(str(e))
    finally:
        writer.close()
        await writer.wait_closed()
        print('Closed the connection')


async def start_server():
    server = await asyncio.start_server(print_data, IP, PORT)
    server_addr = server.sockets[0].getsockname()
    print(f'Serving on {server_addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        print('Started server')
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print('Stopped server')
        os.system('Pause')
        # sys.exit()
