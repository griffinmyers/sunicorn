import socket
import signal
import atexit
import os
import sys

def onexit(acceptor):
    acceptor.close()

def onquit(*args):
    print('So long!')
    sys.exit(1)

def main():
    acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    acceptor.bind(('localhost', 4242))
    acceptor.listen(10)

    atexit.register(onexit, acceptor)

    for i in range(3):
        if os.fork() == 0:
            signal.signal(signal.SIGINT, lambda *args: sys.exit(1))
            pid = os.getpid()
            print('[{0}] child listening on shared socket'.format(pid))

            while True:
                conn, addreess = acceptor.accept()
                conn.sendall('[{0}] echo> '.format(pid))
                data = conn.recv(4096)
                conn.sendall(data)
                conn.close()

            sys.exit(0)

    signal.signal(signal.SIGINT, onquit)
    os.wait()

if __name__ == '__main__':
    main()
