#encoding:utf-8

import string

s="big file is fihewe jowe!"

print s
#capwords()将一个字符串中所有单词的首字母大写
print string.capwords(s)

"""maketrans()函数将创建转换表，可以结合translate()方法将一组字符修改成另外一组
字符修改为另一组字符，这种方法比反复调用replace()更为高效"""
leet=string.maketrans('abegilipestsz','4729230482156')

print s
print s.translate(leet)


