#encoding:utf-8

import os
import sys

FILENAMES=[__file__,
           os.path.dirname(__file__),
           os.getcwd(),
           os.path.abspath(os.path.join(os.curdir)),
           os.path.abspath(os.path.join(os.getcwd(),os.pardir)),
          ]

def Is_file(file):
    print 'File :',file
    print 'Absolute :',os.path.isabs(file)
    print 'Is File? :',os.path.isabs(file)
    print 'Is Dir? :',os.path.isdir(file)
    print 'Is Link? :',os.path.islink(file)
    print 'Mountpoint? :',os.path.ismount(file)
    print 'Exists? :',os.path.exists(file)
    print 'Link Exists? :',os.path.lexists(file)

for file in FILENAMES:
    try:
        Is_file(file)
    except:
        print "error!"