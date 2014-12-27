#encoding: utf-8

import array

a=array.array("B",range(16))
b=array.array("h",range(16))

print a
print repr(a.tostring)

print b
print repr(b.tostring)


