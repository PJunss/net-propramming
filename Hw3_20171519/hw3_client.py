import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print (msg.decode())

sock.send(b'Junhwi Park')

nums = sock.recv(1024)
num = int.from_bytes(nums,'big')
print(num)

sock.close()
