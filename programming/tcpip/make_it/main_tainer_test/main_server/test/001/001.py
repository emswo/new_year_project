import socket, threading

host = '127.0.0.1' #호스팅 IP
port_A = 8022 #A호스팅 port
port_B = 8023 #B호스팅 port
main_server_in_port = 8020 #타겟 IP

def socket_thread(client_socket, addr):
    #서버 내부
    print("connected by", addr)
    #
    try:
        msg = 'i am main server'
        client_socket.send(msg.encode('utf-8'))
        while True:
            data = client_socket.recv(1024)
            msg = data.decode('utf-8')
            print('Recv: ',msg)
            msg = 'echo: '+msg
            client_socket.send(msg.encode('utf-8'))
    except:
        print("excep: ",addr)
    finally:
        client_socket.close()



def going_to_server (ip,port):
    try:
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #서버 소캣 생성
        server_socket.bind((ip,port))
        #서버 시작 (host = 127.0.0.1 , port = 8024)
        server_socket.listen(1)
        #서버 대기
        while True:
            #다중 클라이언트 접속을 위해 무한루프 사용
            client_socket, addr = server_socket.accept()
            #client_socket,addr 튜플로 소켓과 주소를 받음
            server_threading = threading.Thread(target=socket_thread,args=(client_socket,addr))
            #쓰레드로 넘겨줌
            server_threading.start()
            #쓰레드 시작
    except:
        print('sub_server error')
    finally:
        server_socket.close()

sub_A = threading.Thread(target=going_to_server, args=(host,port_A))
sub_A.start()

sub_B = threading.Thread(target=going_to_server, args=(host,port_B))
sub_B.start()

main = threading.Thread(target=going_to_server, args=(host,main_server_in_port))
main.start()
