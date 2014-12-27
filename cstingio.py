#coding=utf-8

import cStringIO

Message="That is my bag!"

file=cStringIO.StringIO(Message)

print file.read()
