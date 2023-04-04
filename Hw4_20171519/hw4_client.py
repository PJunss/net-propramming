from socket import *

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(('localhost', 1111))

while True:
        msg = input('Number:')
        if msg == 'q':
            sock.send(msg.encode())
            break
        sock.send(msg.encode())

        result = sock.recv(1024).decode()
        print(f"{result}")

sock.close()