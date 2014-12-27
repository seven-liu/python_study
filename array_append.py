#encoding: utf-8

import array

a=array.array("B",[1,2,3])

a.append(4)
print a

a=a+a
print a

a=a[2:-2]
print a


print repr(a.tostring())
for i in a:
    print i
