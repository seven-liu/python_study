#encoding:utf-8

import collections

def default_factory():
    return 'default value'

d=collections.defaultdict(default_factory,foo='bar')

print 'd:',d
print 'foo ==>', d['foo']
print 'de ==>', d['de']
