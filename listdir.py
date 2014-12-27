#encoding:utf-8

import os
import os.path
from os.path import isdir,isfile
import sys
import string

basepath="D:\\test"

def listfiles(path):
  files=os.listdir(path)
  list1=[]
  for file in files:
    if file:
      filepath=os.path.join(path,file)
      if isdir(filepath):
        print'%s is dir' %file
        listfiles(filepath)
      else:
        a=os.path.join(path,file)
        print a


DIRs=listfiles(basepath)
print DIRs
#for i in DIRs:
#        print i





