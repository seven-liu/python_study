#encoding:utf-8

import socket
from urlparse import urlparse

for port in [80,443,21,22,70,25,143,993,110,995,465]:
    print urlparse.urlparse((socket.getservbyport(port),'example.com','/','','',''))
