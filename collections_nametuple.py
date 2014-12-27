#encoding:utf-8

import collections

Person=collections.namedtuple('Person','name age gender')



bob = Person(name='bob',age=30,gender='male')
Jane = Person(name='Jane',age=24,gender='female')

for p in [bob,Jane]:
    print '%s is a %d years old %s' %p

