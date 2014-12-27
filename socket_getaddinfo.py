#encoding:utf-8

import socket

def get_constants(prefix):
    return dict((getattr(socket,n),n)
                for n in dir(socket)
                if n.startswith(prefix)
                )

families=get_constants('AF_')
types=get_constants('SOCK_')
protocols=get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.python.org','http'):
    family,socktype,proto,canonname,sockadd=response

    print 'Family :',families[family]
    print 'Type :',types[socktype]
    print 'Protocol :',protocols[proto]
    print 'Canonical name:',canonname
    print 'Socket address:',sockadd
    print