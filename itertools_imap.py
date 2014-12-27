#encoding:utf-8

from itertools import *

print "Doubles:"
for i in imap(lambda x:2*x,xrange(5)):
    print i

print 'Multiples:'
for i in imap(lambda x,y:(x,y,x*y),xrange(5),xrange(5,10)):
    print '%d * %d = %d' %i
