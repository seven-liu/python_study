#coding=utf-8

import os

#for file in os.listdir("d:\download"):
#    print file


cwd=os.getcwd()
print "current path:", cwd
    
#os.chdir(os.pardir)
#print "parent path:",os.getcwd()

#os.chdir(os.pardir)
#print "parent path:",os.getcwd()

#os.chdir("download")
#print "3:",os.getcwd()

#os.chdir("pic")
#print "4:",os.getcwd()


os.makedirs("test")

fp=open("test/abc.txt","w")
fp.write("test!")
fp.close()

try:
    os.remove("test/aabc.txt")
except WindowsError:
    pass

os.remove("/test/abc.txt")
os.removedirs("test")


    
    


    
