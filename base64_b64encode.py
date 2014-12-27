#encoding:utf-8

import base64
import textwrap
import os
import sys

#打开自己
with open(__file__,'rt') as input:
    raw=input.read()
    initial_data=raw.split('#end_pymotw_header')[1]

encoded_data=base64.b64encode(initial_data)
#num=len(initial_data)
print encoded_data
decoded_string=base64.b64decode(encoded_data)
print decoded_string

#padding=3-(num%3)

#print '%d bytes before encoding' %num
#print 'expect %d padding bytes' %padding
#print '%d bytes after encoding' %len(encoded_data)
#print
#print encoded_data