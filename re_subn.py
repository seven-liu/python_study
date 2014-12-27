#encoding:utf-8

import re
bold=re.compile(r'\*{2}(.*?)\*{2}',re.UNICODE)

text='Make this **bold**. This **too**.'

print 'Text:',text
print 'Bold:',bold.subn(r'<b>\1</b>',text)

