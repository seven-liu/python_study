#encoding:utf-8

import socket

#gethostbyname_ex()返回服务器的标准主机名、所有别名，以及可以用来达到这个主机的所有可用IP地址。

for host in ['liu PC','www','www.python.org','www.vulnhunt.com','xxx']:
    print host
    try:
        hostname,aliases,address=socket.gethostbyname_ex(host)
        print ' Hostname: ',hostname
        print ' Aliases: ',aliases
        print ' Address: ',address
    except socket.error,msg:
		print 'Error: ',msg
    print
