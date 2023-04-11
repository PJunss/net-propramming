from socket import *
import time

s1 = socket(AF_INET, SOCK_STREAM)
s1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s1.connect(('localhost', 6666))

s2 = socket(AF_INET, SOCK_STREAM)
s2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s2.connect(('localhost', 6667))

while True:
    servernum = input("연결할 서버를 선택해주십시요 (1 or 2) : ")
    if servernum == "1":
        expression = "Request"
        s1.sendall(expression.encode("utf-8"))
        data = s1.recv(1024)
        data_list = data.decode().split()
        temp = data_list[0]
        humid = data_list[1]
        illum = data_list[2]
        result_str = "Server1 : {} Temp : {} Humid : {} illum : {}\n".format(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), temp, humid, illum)
        print(result_str)
        with open("data.txt", "a") as f:
            f.write(result_str)

    elif servernum == "2":
        expression = "Request"
        s2.sendall(expression.encode("utf-8"))
        data = s2.recv(1024)
        data_list = data.decode().split()
        heartbeat = data_list[0]
        steps = data_list[1]
        cal = data_list[2]
        result_str = "Server2 : {} Heartbeat : {} Steps : {} Cal : {}\n".format(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), heartbeat, steps, cal)
        print(result_str)
        with open("data.txt", "a") as f:
            f.write(result_str)

    else:
        print("잘못 입력하셨습니다")

    if servernum == "quit":
        s1.close()
        s2.close()
        exit()