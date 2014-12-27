#encoding:utf-8

import zlib

original_data='This is the original text you have good choicespython bzip_test examples.'

fmt='%15s %15s'
print fmt %('len(data)','len(compressed)')
print fmt %('-'*15,'-'*15)

for i in xrange(5):
    data=original_data*i
    compressed=zlib.compress(data)
    highlight='*' if len(data)<len(compressed) else ''
    print fmt %(len(data),len(compressed)),highlight


