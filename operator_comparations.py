#encoding utf-8

from operator import *


def compare2num(x,y):
    print x,y

    for func in (lt,le,eq,ne,ge,gt):
        print '%s(a,b):'%func.__name__,func(a,b)

a=3
b=5
compare2num(a,b)

