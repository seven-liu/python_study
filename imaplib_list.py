#encoding:utf-8

import imaplib
from pprint import pprint
from imaplib_connect import open_connection

c=open_connection()
try:
    typ,data=c.list()
    print 'Response code:',typ
    print 'Response:'
    pprint(data)
finally:
    c.logout()
