#encoding:utf-8

import re

#re正则表达式，常用于搜索文本中的模式。

pattern='this'
text='Does this text match the pattern?'

match=re.search(pattern,text)

s=match.start()
e=match.end()

print 'Found "%s"\nin "%s"\nfromm %d to %d ("%s")' %\
 (match.re.pattern,match.string,s,e,text[s:e])

