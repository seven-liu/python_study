#encoding:utf-8

import codecs
import sys

def _codecs_err(file):
    error_handling=sys.argv[1]
    try:
        with codecs.open('encode_error.txt','w',
                          encoding='ascii',
                          errors=error_handling) as f:
                f.write(file)
    except UnicodeEncodeError,err:
        print 'ERROR:',err
    else:
        with open('encode_error.txt','rb') as f:
            print 'File contents: ',repr(f.read())

a=u'pi :\u03c0'
_codecs_err(a)
