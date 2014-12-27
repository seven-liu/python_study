#encoding:utf-8

import tarfile
from contextlib import closing

print 'creating archive'
with closing(tarfile.open('test.tar',mode='w'))as out:
    print 'add README.txt'
    out.add('test.txt')

print
print 'Contents:'
with closing(tarfile.open('test.tar',mode='r'))as t:
    for member_info in t.getmembers():
        print member_info.name
