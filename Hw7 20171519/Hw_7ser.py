import socket
import threading

def handler(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"[{addr}] {data.decode()}")
        for client_conn in clients:
            if client_conn != conn:
                client_conn.sendall(data)
    conn.close()
    clients.remove(conn)

server_addr = ('localhost', 2500)
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(server_addr)
server_sock.listen()
print('Server Started')

clients = []

while True:
    client_conn, client_addr = server_sock.accept()
    print(f"new client {client_addr}")
    clients.append(client_conn)
    th = threading.Thread(target=handler, args=(client_conn, client_addr))
    th.daemon = True
    th.start()
