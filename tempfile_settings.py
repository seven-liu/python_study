#encoding:utf-8

import tempfile
from shutil import *
from commands import *
import os

print 'gettempdir():',tempfile.gettempdir()
print 'gettempprefix():',tempfile.gettempprefix()


with open('file_to_change.txt','w') as f:
    f.write('tests!')
os.chmod('file_to_change.txt',0444)
print 'BEFORE:'
print getstatus('file_to_change.txt')
copymode('crypt.py','file_to_change.txt')
print 'After:'
print getstatus('file_to_change.txt')

