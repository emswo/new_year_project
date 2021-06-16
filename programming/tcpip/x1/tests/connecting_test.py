from socket import *
import threading

ip = '127.0.0.1'
port_in = 10001
port_out_A = 10010
port_out_B = 10100

class _in (threading.Thread):
    def run(self) -> None:
        clientSocket = socket(AF_INET,SOCK_STREAM) #소켓 생성
        clientSocket.connect((ip,port_in)) #서버와 연결
        print('connect [server_in] success')

class _A (threading.Thread):
    def run(self) -> None:
        clientSocket = socket(AF_INET,SOCK_STREAM) #소켓 생성
        clientSocket.connect((ip,port_out_A)) #서버와 연결
        print('connect [server_A] success')  

class _B (threading.Thread):
    def run(self) -> None:
        clientSocket = socket(AF_INET,SOCK_STREAM) #소켓 생성
        clientSocket.connect((ip,port_out_B)) #서버와 연결
        print('connect [server_B] success')
   
# clientSocket.send("i am a client".encode("utf-8")) #데이터 송신
# print("put messege is success")
# data = clientSocket.recv(1024) #데이터 수신
# print("send: ",data.decode('utf-8'))
# clientSocket.close() #연결종료

t_in = _in()
t_in.start()
t_A = _A()
t_A.start()
t_B = _B()
t_B.start()
