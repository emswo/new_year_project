import socket, threading
host = '127.0.0.1' #호스팅 IP
port = 8024 #호스팅 port

def socket_thread(client_socket, addr):
    print("connected by", addr)
    try:
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

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(1)

try:
    while True:
        client_socket, addr = server_socket.accept()
        server_threading = threading.Thread(target=socket_thread,args=(client_socket,addr))
        server_threading.start()
except:
    print('server error')
finally:
    server_socket.close()