#coding=utf-8

import os
import shutil

os.mkdir("backup")

for file in os.listdir("."):
    if os.path.splitext(file)[1]==".py":
        print file
        shutil.copy(file,os.path.join("backup",file))
    
try:
    os.remove("test")
except OSError,error:
    print "errors: %s",error
    
