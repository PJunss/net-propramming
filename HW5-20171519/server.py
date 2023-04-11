from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(('', 80))

s.listen(10)

print("waiting")

while True:

    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    try:
        path = req[0].split()[1]

        if path == '/index.html':
            with open('index.html', 'rb') as f:
                content = f.read()
            mime_type = 'text/html; charset=UTF-8'
        elif path == '/iot.png':
            with open('iot.png', 'rb') as f:
                content = f.read()
            mime_type = 'image/png'
        elif path == '/favicon.ico':
            with open('favicon.ico', 'rb') as f:
                content = f.read()
            mime_type = 'image/x-icon'
        else:
            raise FileNotFoundError

        header = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\nContent-Length: {len(content)}\r\n\r\n"
        c.send(header.encode())
        c.send(content)

    except FileNotFoundError:
        c.send(b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n")
        c.send(b"<html><body><h1>Not Found</h1></body></html>")

    c.close()
