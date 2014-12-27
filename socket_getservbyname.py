#encoding:utf-8

import socket
from urlparse import urlparse

for url in ['https://192.168.12.34',
            'https://www.mybank.com',
            'ftp://192.168.12.50'
            'smtp://exmail.qq.com',
            'imap://exmail.qq.com',
            'pop3://exmail.qq.com'
    ]:
    parsed_url=urlparse(url)
    port=socket.getservbyname(parsed_url.scheme)
    print '%6s:%s' %(parsed_url.scheme,port)