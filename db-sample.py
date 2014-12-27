#encoding:utf-8

import anydbm

db=anydbm.open("database","c")
db["1"]="one"
db["2"]="two"
db["3"]="three"

db.close()

db=anydbm.open("database","r")
for key in db.keys():
    print repr(key),repr(db[key])
