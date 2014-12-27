#encoding:utf-8

from urlparse import urlparse
import sys
import os

url='http://www.vulnhunt.com'

def urlparse_url(urls):

  parsed=urlparse(urls)
  print 'scheme :',parsed.scheme
  print 'netloc :',parsed.netloc
  print 'path :',parsed.path
  print 'params :',parsed.params
  print 'query :',parsed.query
  print 'fragment :',parsed.fragment
  print 'username :',parsed.username
  print 'password :',parsed.password
  print 'hostname :',parsed.hostname,'(netloc in lowercase)'
  print 'port :',parsed.port

urlparse_url(url)
