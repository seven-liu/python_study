#encoding:utf-8

import functools
import inspect
from pprint import pprint

class Myobject(object):
    def __init__(self,val):
        self.val=val
    def __eq__(self,other):
        print ' testing __eq__(%s,%s)' %(self.val,other.val)
        return self.val==other.val
    def __gt__(self,other):
        print 'testing __gt__(%s,%s)' %(self.val,other.val)
        return self.val>other.val

print 'Methods:\n'
pprint(inspect.getmembers(Myobject,inspect.ismethod))

a=Myobject(1)
b=Myobject(2)

print '\nComparisions:'
for expr in ['a<b','a==b','a>b','a>=b','a<=b']:
    print '\n%-6s:' %expr
    result=eval(expr)
    print 'result of %s:%s' %(expr,result)



