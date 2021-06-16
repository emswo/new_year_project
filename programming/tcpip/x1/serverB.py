from socket import *
import threading

host = '127.0.0.1' #서버 ip
server_in_socket_log = open("server_in_trapic_B.txt",'a') #서버 로그파일 열기
def thread_run(port): #쓰레드에 넣을 함수
    server_in_socket = socket(AF_INET,SOCK_STREAM) #ipv4, tcp 소캣 만들기
    server_in_socket.bind((host,port)) #ip와 port를 지정
    server_in_socket.listen(1)#연결대기
    #time = noc()
    server_in_socket_log.write(f'listenning {port}\n') #대기중 출력
    print(f'listenning {port}\n') #대기중 출력
    connectionSocket = 0 #연결정보 받을 변수 초기화
    addr = 0 #연결정보 받을 변수 초기화
    #while connectionSocket+addr == 0:
    connectionSocket,addr = server_in_socket.accept()#연결정보 받기
    server_in_socket_log.write(f'connecting {port}\n')#연결됨 출력
    print(f'connecting {port}\n')#연결됨 출력
    #noc()
    print(list(addr),'\n')#연결정보 출력
    #while range(0,10):
    #try:
    
    server_in_socket.send("i am a client: [B]".encode("utf-8")) #데이터 송신
    #    server_in_socket_log.write('send success 0000\n')
    #except:
    #    server_in_socket_log.write('send failuer FFFF\n')
        #data = connectionSocket.recv(1024) #데이터 수신, 최대 1024
        ##print("recv: ",data.decode('utf-8')) #받은 데이터 UTF-8
        #for _ in range(0,101):
    #server_in_socket.send("close".encode("utf-8")) #닫기
    data_in = server_in_socket.recv(1024) #데이터 수신
    print(data_in.decode('utf-8')) #수신된 데이터 출력
    #while data_in != 0 : #데이터 받았으면
    server_in_socket.close() #서버를 닫는다
#threading.Thread(target=thread_run, args=(10100,)).start

for k in range(8101,8201): #8101포트부터 8201포트까지 소캣을 연결한다
    try:
        threading.Thread(target=thread_run, args=(k,)).daemon = False #데몬 끄기
        threading.Thread(target=thread_run, args=(k,)).start() #소캣 시작
    except: #에러 회피
        pass

