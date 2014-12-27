#encoding:utf-8

import anydbm

db=anydbm.open('example.db','r')
try:
    print 'Keys():',db.keys()
    for k,v in db.iteritems():
        print 'iterating:',k,v
    print 'db["author"]=',db['author']
finally:
    db.close()
