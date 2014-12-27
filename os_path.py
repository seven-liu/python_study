#encoding:utf-8

import os
import sys

f=os.getcwd()
print f

print "curdir:",os.path.abspath(os.path.join(os.curdir))
print "pardir:",os.path.abspath(os.path.join(f,os.pardir))

print "extsep:",os.path.abspath(os.path.join(os.extsep))

