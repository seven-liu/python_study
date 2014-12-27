#encoding:utf-8

import socket
import sys

messages=['This is the message.',
         'It will be sent',
         'In parts.']

server_address=('localhost',10000)
socks=[socket.socket(socket.AF_INET,socket.SOCK_STREAM),
       socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       ]

print >>sys.stderr,'connecting to %s port %s' %server_address
for s in socks:
    s.connect(server_address)


for message in messages:
    for s in socks:
        print >>sys.stderr,'%s:sending "%s"' %(s.getsockname(),message)
        s.send(message)

    for s in socks:
        data=s.recv(1024)
        print >>sys.stderr,'closing socket',s.getsockname()
        s.close()



