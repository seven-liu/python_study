#encoding:utf-8

import socket
#gethostbyname()访问操作系统主机名解析API，将服务器名字转换为其数字地址

print socket.gethostname()

for host in ['www.baidu.com','www','www.python.org','xxxx']:
    try:
        print '%s:%s' %(host,socket.gethostbyname(host))
        print '%s:%s' %(host,socket.gethostbyaddr(host))
        print '%s:%s' %(host,socket.getnameinfo(host))
        print '%s:%s' %(host,socket.getprotobyname(host))
        print '%s:%s' %(host,socket.getservbyname(host))
    except socket.error,msg:
        print '%s:%s' %(host,msg)


