#encoding:utf-8

import socket
import sys

#客户端不绑定一个端口并监听，而是使用connet()将套接字直接关联到远程地址。

#create a TCP/IP socket
#sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to the socket to the port where the server is listening

#server_address=('localhost',10000)
#print >>sys.stderr,'connectiong to %s port %s' %server_address
#sock.connect(server_address)

#上面几个步骤可以直接用这句简易连接替代
sock=socket.create_connection(('localhost',10000))

#recv()从连接读取，并用sendall()传输
try:
    #send data
    message='This is the message.It will be repeated/'
    print >>sys.stderr,'sending "%s"' %message
    sock.sendall(message)

    #look for the response
    amount_received=0
    amount_expected=len(message)

    while amount_received<amount_expected:
        data=sock.recv(16)
        amount_received+=len(data)
        print >>sys.stderr,'received "%s"' %data

finally:
    print >>sys.stderr,'closing socket'
    sock.close()
