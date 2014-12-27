#encoding:utf-8

import anydbm

db=anydbm.open('sample.db','n')
try:
    db[1]='one'
except TypeError ,err:
    print '%s: %s' %(err.__class__.__name__,err)
finally:
    db.close()
