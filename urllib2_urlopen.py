#encoding:utf-8

import urllib2

response=urllib2.urlopen('http://www.baidu.com/')
#print 'RESPONSE:',response
#print 'URL:',response.geturl()
for line in response:
    print line.rstrip()

headers=response.info()
print 'DATA :',headers['date']
print 'HEADERS :'
print '--------------'
print headers

data=response.read()
print 'LENGTH :',len(data)
print 'DATA :'
print '-----------'
print data


