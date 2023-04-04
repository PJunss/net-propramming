from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(('', 1111))
s.listen(5)
print('waiting')

def calculate(expr):
        try:
            result = eval(expr)
            return round(result, 1)

        except:
            return "Error"

while True:
    client, addr = s.accept()
    print('connection from ', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        result = calculate(data.decode())
        client.send(str(result).encode())

        client.close()
    s.close()
