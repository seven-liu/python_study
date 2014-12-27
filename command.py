#encoding: utf-8

import commands

stat,output=commands.getstatusoutput("dir")

print "status","=",stat
print "output","=",len(output),"bytes"

