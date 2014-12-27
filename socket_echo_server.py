#encoding:utf-8

import socket
import sys

#create a TCP/IP socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind()将这个套接字与服务器地址管理，包含地址和端口
server_address=('localhost',10000)
#也可以用sock.getsockname()监听所有端口，而不是指定端口
print >>sys.stderr,'starting up on %s port %s' %server_address

sock.bind(server_address)

#listen()将这个套接字设置为服务器模式，调用accept()等待到来的连接。
#listen for incoming connections
sock.listen(1)

#上面几步直接用简易连接可以直接替代
#sock=socket.create_connection(('localhost',10000))

while True:
    #wait for connection
    print >>sys.stderr,'waiting for a connection.'
    connection,client_address=sock.accept()

#recv()从连接读取，并用sendall()传输
    try:
        print >>sys.stderr,'connection from',client_address
        #receive the data in samll chunks and retransmit it
        while True:
            data=connection.recv(16)
            print >>sys.stderr,'receeived "%s"' %data
            if data:
                print >>sys.stderr,'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr,'no data from',client_address
                break

    finally:
        #clean up connection
        connection.close()
