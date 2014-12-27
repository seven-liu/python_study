#encoding:utf-8

import collections

c=collections.Counter('abcddaadddcb')

for letter in 'abcde':
    print '%s: %d' %(letter,c[letter])

