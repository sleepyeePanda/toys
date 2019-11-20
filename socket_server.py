import socket
import os
import sys


HOST = '192.168.0.10'
PORT = 5000

BUF_SIZE = 24


def run_server():
    print('Started server.')
    with socket.socket() as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()
        print(f'Serving on {HOST}:{PORT}')

        try:
            while True:
                data = conn.recv(BUF_SIZE)
                print(f'Received {data.hex()} from {addr[0]}:{addr[1]}')
        except Exception as e:
            print(str(e))
        finally:
            conn.close()
            print('Closed the connection.')


if __name__ == '__main__':
    try:
        run_server()
    except KeyboardInterrupt:
        print('Stopped server.')
        os.system('pause')
        # sys.exit()
