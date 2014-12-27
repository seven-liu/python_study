#coding=utf-8

import os
import shutil
import hashlib
import md5
import string,random
import pwd,crypt


#def getsalt(chars=string.letters+string.digits):
#return random.choice(chars)+random.choice(chars)

#print crypt.crypt("apple",getsalt)


def login(user,password):
   try:
      pw1=pwd.getpwnam(user)[1]
      pw2=crypt.crypt(password,pw1[:2])
      return pw1==pw2
   except KeyError,error:
      print "Password is wrong! %s",error
      return 0

user=raw_input("username:")
password=raw_input("password:")

if login(user,password):
   print "welcome! %s login success!",user
else:
   print "login failed!please try again."
   


    
