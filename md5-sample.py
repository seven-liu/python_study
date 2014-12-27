#coding=utf-8

import md5
import string
import base64
import os
import sys
import hashlib

hash= hashlib.md5()
hash.update("abcdefg")

value=hash.digest()
print hash.hexdigest()

print base64.encodestring(value)

