#encoding:utf-8
import binascii
import socket
import struct
import sys

#inet_aton():IPV4转化为二进制。inet_ntoa()相反。

for string_address in ['192.168.12.1','127.0.0.1']:
    packed=socket.inet_aton(string_address)
    print 'original:',string_address
    print 'packed:',binascii.hexlify(packed)
    print 'unpacked:',socket.inet_ntoa(packed)
    print

#inet_pton():IPV4或6转化为二进制。inet_ntop()相反。

string_address1=['fe80::65b5:9edd:533a:5fe8%18','fe80::210:18ff:fee0:7f94/64']

for string_address in string_address1:
    packed=socket.inet_pton(socket.AF_INET6,string_address)
    print 'original:',string_address
    print 'packed:',binascii.hexlify(packed)
    print 'unpacked:',socket.inet_ntoP(socket.AF_INET6,packed)
    print
