#encoding:utf-8

import string

values={'var':'foo'}

#由于values字典中没有对应的missing值，因此substitute()会产生一个KeyError.
#但是safe_substitute()不会抛出错误，他将捕获异常，并在文本中保留变量表达式。
t=string.Template("$var is here but $missing is not provided")

try:
    print 'substitute() :',t.substitute(values)
except KeyError,err:
    print 'ERROR:',str(err)

print 'safe_substitute():',t.safe_substitute(values)


