#encoding: utf-8

import anydbm
import whichdb

db=anydbm.open('example.db','n')
db['key']='value'
db['today']='Sunday'
db['author']='Dongu'
db.close()

print whichdb.whichdb('example.db')
