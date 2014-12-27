#encoding:utf-8
import os
import os.path
import pprint

for name in os.getcwd() as f:
    subname=os.path.join(f,name)
    if os.path.isdir(subname):
        print ' %s/' %name
    print '%s' %name
print

