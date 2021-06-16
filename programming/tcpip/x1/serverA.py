from socket import *
import threading

host = '127.0.0.1'

def thread_run(port):
    server_in_socket_log = open("server_in_trapic_A.txt",'a')
    
    server_in_socket = socket(AF_INET,SOCK_STREAM)
    server_in_socket.bind((host,port))
    server_in_socket.listen(1)
    #time = noc()
    server_in_socket_log.write(f'listenning: {port}\n')
    
    connectionSocket,addr = server_in_socket.accept()
    server_in_socket_log.write(f'connecting: {port}\n')
    #noc()
    print(list(addr))
    #while range(0,10):
    server_in_socket.send(f"i am a client: [A]".encode("utf-8")) #데이터 송신
        #data = connectionSocket.recv(1024) #데이터 수신, 최대 1024
        ##print("recv: ",data.decode('utf-8')) #받은 데이터 UTF-8
        #for _ in range(0,101):
    #server_in_socket.send("close".encode("utf-8")) #닫기
    server_in_socket.close()

threading.Thread(target=thread_run, args=(10100,)).start

for k in range(8000,8101):
    try:
        threading.Thread(target=thread_run, args=(k,)).start()
    except:
        pass
