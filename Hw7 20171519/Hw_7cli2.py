import socket
import threading

def recv_handler(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())

server_addr = ('localhost', 2500)
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_id = input('ID를 입력하세요: ')
client_sock.connect(server_addr)
client_sock.sendall(my_id.encode())

th = threading.Thread(target=recv_handler, args=(client_sock,))
th.daemon = True
th.start()

while True:
    data = input()
    client_sock.sendall(f"[{my_id}] {data}".encode())
