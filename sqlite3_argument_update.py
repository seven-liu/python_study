#encoding:utf-8

import sqlite3
import sys
import os

#带变量查询SQL语句
db_filename='todo.db'
id=int(sys.argv[1])
status=sys.argv[2]

conn=sqlite3.connect(db_filename)
cursor=conn.cursor()
query_cmd="update task set status=:status where id=:id"
cursor.execute(query_cmd,{'status':status,'id':id})

