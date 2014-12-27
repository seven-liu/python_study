#encoding:utf-8

try:
    import cpickle as pickle
except:
    import pickle
import pprint



data=[{'a':'A','b':2.0,'c':2.5}]
print 'BEFORE Date:',
pprint.pprint(data)

#pickle只包含ASCII字符
data_string=pickle.dumps(data)
data2=pickle.loads(data_string)
print 'AFTER pickle: ',
pprint.pprint(data2)


print 'SAME?:',(data is data2)
print 'EQL?:',(data==data2)

