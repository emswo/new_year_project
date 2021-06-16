from socket import *
import threading
ip = '127.0.0.1'
port = 10001

clientSocket = socket(AF_INET,SOCK_STREAM) #소켓 생성
clientSocket.connect((ip,port)) #서버와 연결
print('connect success')

class in_A (threading.Thread):
    #while True:
        clientSocket.send("i am a client [A]".encode("utf-8")) #데이터 송신
        print("put messege A is success")
class in_B (threading.Thread):
    #while True:
        clientSocket.send("i am a client [B]".encode("utf-8")) #데이터 송신
        print("put messege B is success")

t_in_A = in_A()
t_in_A.start()
t_in_B = in_B()
t_in_B.start()
t_in_A.join()
t_in_B.join()
while True:
    t_in_A.join()
    t_in_B.join()


#data = clientSocket.recv(1024) #데이터 수신
#print("send: ",data.decode('utf-8'))
clientSocket.close() #연결종료