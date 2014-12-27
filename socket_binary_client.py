#encoding:utf-8

#发送二进制。二进制传输数据，要用struct把他们打包到一个缓冲区。

import binascii
import socket
import struct
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',10000)
sock.connect(server_address)
values=(1,'abc',2.4)

#packer解释器，struct打包并指明数据类型
packer=struct.Struct('I 2s f')
packed_data=packer.pack(*values)
print 'values=',values

try:
    #send data
    print >>sys.stderr,'sending %r' %binascii.hexlify(packed_data)
    sock.sendall(packed_data)

finally:
    print >>sys.stderr,'closing socket'
    sock.close()