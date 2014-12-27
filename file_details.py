#encoding:utf-8

import os
import time

def Access_times(file):
    filename=file
    access_time=time.ctime(os.path.getatime(file))
    modified_time=time.ctime(os.path.getmtime(file))
    change_time=time.ctime(os.path.getctime(file))
    file_size=os.path.getsize(file)

    print 'file details:'
    print 'filename: ',filename
    print 'access_time: ',access_time
    print 'modified_time: ',modified_time
    print 'change_time: ',change_time
    print 'file_size: ',file_size



f=[]
for item in os.listdir(os.getcwd()):
    f.append(item)
    print f
    Access_times(item)
    break