#encoding:utf-8

import os
import sqlite3





db_filename='todo.db'
schema_filename='todo_schema.sql'

db_is_new=not os.path.exists(db_filename)



with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print "creating schema"
        with open(schema_filename,'rt') as f:
            schema=f.read()
        conn.executescript(schema)

        print "Inserting initial data"
        conn.executescript("""
        insert into project (name,description,deadline)
        values('pymotw','python module of the week','2010-11-01');

        insert into task (details,status,deadline,project)
        values('write about select','done','2010-10-02','pymotw');

        insert into task (details,status,deadline,project)
        values('write about random','waiting','2010-10-10','pymotw');

        insert into task (details,status,deadline,project)
        values('write about sqlite3','active','2010-10-18','pymotw');
        """)
    else:
        print 'Database exists,assume schema does,too.'
