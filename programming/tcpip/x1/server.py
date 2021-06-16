import threading
import sys
from datetime import datetime
from socket import *

host = '127.0.0.1'
port_in = 10001
port_out_A = 10010
port_out_B = 10100

def noc():
    now = datetime.now()
    print('[',now.year,'-',now.month,'-',now.day,' ',now.hour,':',now.minute,':',now.second,']')
    #p = str(print('[',now.year,'-',now.month,'-',now.day,' ',now.hour,':',now.minute,':',now.second,']'))
    #return p

class thread_in(threading.Thread):
    def run(self) -> None:
        server_in_socket_log = open("server_in_trapic.txt",'w')
        
        server_in_socket = socket(AF_INET,SOCK_STREAM)
        server_in_socket.bind((host,port_in))
        server_in_socket.listen(1)
        
        server_in_socket_log.write('listenning')
        noc()
        connectionSocket,addr = server_in_socket.accept()
        server_in_socket_log.write('connecting')
        noc()
        print(addr)
        while True:
            data = connectionSocket.recv(1024) #데이터 수신, 최대 1024
            print("recv: ",data.decode('utf-8')) #받은 데이터 UTF-8


class thread_out_A (threading.Thread):
    def run(self) -> None:
        server_out_A_socket_log = open("server_out_A_trapic.txt",'w')
        server_out_A_socket = socket(AF_INET,SOCK_STREAM)
        server_out_A_socket.bind((host,port_out_A))
        server_out_A_socket.listen(1)
        
        server_out_A_socket_log.write('listenning')
        noc()
        connectionSocket,addr = server_out_A_socket.accept()
        server_out_A_socket_log.write('connecting')
        noc()
        print(addr)
        
        while True:
            data = connectionSocket.recv(1024) #데이터 수신, 최대 1024
            print("recv: ",data.decode('utf-8')) #받은 데이터 UTF-8

class thread_out_B (threading.Thread):
    def run(self) -> None:
        server_out_B_socket_log = open("server_out_B_trapic.txt",'w')
        server_out_B_socket = socket(AF_INET,SOCK_STREAM)
        server_out_B_socket.bind((host,port_out_B))
        server_out_B_socket.listen(1)
        
        server_out_B_socket_log.write('listenning')
        noc()
        connectionSocket,addr = server_out_B_socket.accept()
        server_out_B_socket_log.write('connecting')
        noc()
        print(addr)
        while True: pass

t_in = thread_in()
t_in.start()
t_out_A = thread_out_A()
t_out_A.daemon = False
t_out_A.start()
t_out_B = thread_out_B()
t_out_B.daemon = False
t_out_B.start()

