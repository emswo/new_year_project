from socket import *
import threading

host = '127.0.0.1' #서버 ip

def thread_run(port):
    clientSocket = socket(AF_INET,SOCK_STREAM) #소켓 생성
    clientSocket.connect((host,port)) #서버와 연결
    ho = open('cllogB.txt','a') #로그파일을 연다
    while True:
        print(f'connect [{port}] success') #포트 연결확인
        data = 0 #데이터 초기화
        data = clientSocket.recv(1024) #데이터 수신
        decoding_data = data.decode('utf-8') #수신된 데이터를 문자열로 변환해서 저장한다
        ho.write(f'[{port}] : {decoding_data}\n') #저장된 데이터를 출력한다
        clientSocket.send('test\n'.encode('utf-8')) #test를 보낸다
        if data != 0: #데이터가 0이 아닐때
            clientSocket.close() #소캣을 닫는다
            break
        #print("send: ",data.decode('utf-8'))
        # if data.decode('utf-8') == 'close':
        #     clientSocket.close() #연결종료
        #     break 
        # else:
        #     pass
    

for k in range(8101,8201): #8101포트부터 8201포트까지 소캣을 연결한다
    try:
        threading.Thread(target=thread_run, args=(k,)).daemon = False #데몬 끄기
        threading.Thread(target=thread_run, args=(k,)).start() #소캣 시작
    except: #에러 회피
        pass
    