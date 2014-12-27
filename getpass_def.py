#encoding:utf-8
import getpass
import sys

try:
#p=getpass.getpass(prompt='what is your color?\n')
 p=getpass.getpass(stream=sys.stderr)
except Exception,err:
    print 'ERROR:',err
else:
    print "you entered:",p