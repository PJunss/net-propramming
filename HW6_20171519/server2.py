from socket import *
import random
import time

def get_data():
    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)
    return f"{heartbeat} {steps} {cal}"

s2 = socket(AF_INET, SOCK_STREAM)
s2.bind(('localhost', 6667))
s2.listen(1)

while True:
    conn, addr = s2.accept()
    print(f"Connected by {addr}")
    while True: 
        data = conn.recv(1024)
        if not data:
            break
        else:
            if data.decode() == "Request":
                expression = get_data()
                conn.sendall(expression.encode())
                time.sleep(1)
            else:
                conn.sendall(b"Invalid request")

    conn.close()

