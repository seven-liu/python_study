#encoding:utf-8

import profile

def func1():
    for i in range(1000):
        pass


def func2():
    for i in range(1000):
        func1()

profile.run("func2()")
