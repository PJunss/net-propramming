from socket import *
import random
import time

def get_data():
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    illum = random.randint(70, 150)
    return f"{temp} {humid} {illum}"

s1 = socket(AF_INET, SOCK_STREAM)
s1.bind(('localhost', 6666))
s1.listen(1)

while True:
    conn, addr = s1.accept()
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