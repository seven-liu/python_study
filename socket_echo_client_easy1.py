#encoding:utf-8

import socket
import sys

sock=socket.create_connection(('localhost',10000))
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
