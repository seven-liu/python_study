#coding=utf-8

import os
import time

file="os-listfile.py"

def filestat(stat):
    mode,ino,dev,nlink,uid,gid,size,atime,mtime,ctime=stat
    print "-size:",size,"bytes"
    print "-ower:",uid,gid
    print "-created:",time.ctime(ctime)
    print "-last accessed:",time.ctime(atime)
    print "-last modified:",time.ctime(mtime)
    print "-mode:",oct(mode)
    print "-inode/dev:",ino,dev


stat=os.stat(file)
print "stat",file

filestat(stat)

 

fp=open(file)
stat=os.fstat(fp.fileno())
print "fstat",file
filestat(stat)
