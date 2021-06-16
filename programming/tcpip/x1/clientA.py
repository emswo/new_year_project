from socket import *
import threading

host = '127.0.0.1'

def thread_run(port):
    clientSocket = socket(AF_INET,SOCK_STREAM) #소켓 생성
    clientSocket.connect((host,port)) #서버와 연결
    ho = open('cllogA.txt','a')
    while True:
        print(f'connect [{port-8000}] success')
        data = clientSocket.recv(1024) #데이터 수신
        ho.write(f'[{port}] :7 {str(data.decode("utf-8"))}\n')
        break
        #print("send: ",data.decode('utf-8'))
        if data.decode('utf-8') == 'close':
            clientSocket.close() #연결종료
            break 
        else:
            pass
    

for k in range(8000,8101):
    try:
        threading.Thread(target=thread_run, args=(k,)).daemon = True
        threading.Thread(target=thread_run, args=(k,)).start()
    except:
        pass
    