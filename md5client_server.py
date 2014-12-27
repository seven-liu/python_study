#coding=utf-8

import os
import shutil
import hashlib
import md5
import string,random


def getchallenge():
    
   challenge=map(lambda i:chr(random.randint(0,255)),range(16))
   return string.join(challenge,"")


def getresponse(password,challenge):

    m=hashlib.md5()
    m.update(password)
    m.update(challenge)
    return m.digest()


print "client:","connect"
challenge=getchallenge()
print "server:",repr(challenge)

client_response=getresponse("trustnol",challenge)
print "client:",repr(client_response)


server_response=getresponse("trustnol",challenge)

if server_response==client_response:
    print "server:","login OK"

    
