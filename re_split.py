#encoding:utf-8

import re

text='''Paragraph one
on tow lines.

Paragraph two.

Paragraph three.'''

print 'with findall:'
for num,para in enumerate(re.findall(r'(.+?)(\n{2,}|$)',
                                     text,
                                     flags=re.DOTALL)):
     print num,repr(para)
     print

print
print 'with split:'
for num,para in enumerate(re.split(r'\n{2,}',text)):
    print num,repr(para)
    print