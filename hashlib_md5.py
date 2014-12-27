import hashlib
from hashlib_data import lorem


h=hashlib.md5()
h.update(lorem)
print h.hexdigest()


h=hashlib.sha1()
h.update(lorem)
print h.hexdigest()

