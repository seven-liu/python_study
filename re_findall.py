#encoding:utf-8
import re


text='abcaaebescccaefweaabbbccdeabaaaaccababababaaa'

pattern='ab'

#findall()返回输入中与模式匹配而不重叠的所有字串
#for match in re.findall(pattern,text):

#finditer()会返回一个迭代器，他将生成Match实例，显示原字符串中的位置
for match in re.finditer(pattern,text):
    s=match.start()
    e=match.end()
    print 'Found "%s" at %d:%d' %(text[s:e],s,e)





