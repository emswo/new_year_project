#클라이언트 테스트
from socket import *
import threading

s_socket = socket(AF_INET, SOCK_STREAM)
bufsize = 1024
host = '127.0.0.1'
port = 5001
s_socket.connect((host,port))
st = input("전송 ")
s_socket.send(st.encode('utf-8'))
aa=s_socket.recv(bufsize)
print(aa.decode('utf-8'))
s_socket.close()