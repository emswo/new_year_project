import threading
import sys
from datetime import datetime
from socket import *

host = '127.0.0.1'
port_in = 10001
port_out_A = 10010
port_out_B = 10011

def noc():
    now = datetime.now()
    print('[',now.year,'-',now.month,'-',now.day,' ',now.hour,':',now.minute,':',now.second,']')
    p = str(print('[',now.year,'-',now.month,'-',now.day,' ',now.hour,':',now.minute,':',now.second,']'))
    return p

def thread_run(port):
    server_in_socket_log = open("server_in_trapic.txt",'w')
    
    server_in_socket = socket(AF_INET,SOCK_STREAM)
    server_in_socket.bind((host,port))
    server_in_socket.listen(1)
    time = noc()
    server_in_socket_log.write(f'listenning{time}')
    
    connectionSocket,addr = server_in_socket.accept()
    server_in_socket_log.write('connecting')
    noc()
    print(addr)
    while True:
        data = connectionSocket.recv(1024) #데이터 수신, 최대 1024
        print("recv: ",data.decode('utf-8')) #받은 데이터 UTF-8

if __name__ == "__main__":
    threading.Thread(target=thread_run, args=(port_in,)).start()
    threading.Thread(target=thread_run, args=(port_out_A,)).start()
    threading.Thread(target=thread_run, args=(port_out_B,)).start()

    #for k in range(10100,10200):
    #    threading.Thread(target=thread_run, args=(k,)).start()