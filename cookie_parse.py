#encoding:utf-8

import Cookie

HTTP_COOKIE=';'.join(
  [r'integer=5',
   r'string_with_quotes="He said,\"Hello,world!\""'
  ])
print 'From constructor:'
c=Cookie.SimpleCookie(HTTP_COOKIE)
print c

print
print'From load():'
c=Cookie.SimpleCookie(HTTP_COOKIE)
c.load(HTTP_COOKIE)
print c