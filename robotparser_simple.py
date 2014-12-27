#encoding:utf-8

import robotparser
import urlparse

AGENT_NAME='PyMOTW'
URL_BASE='http://www.doughellmann.com/'
parser=robotparser.RobotFileParser()
parser.set_url(urlparse.urljoin(URL_BASE,'robot.txt'))
parser.read()

PATH=[
  '/',
  '/PyMOTW/',
  '/admin/'
  '/downloads/PyMOTW-1.92.tar.gz'
]

for path in PATH:
    print '%6s:%s' %(parser.can_fetch(AGENT_NAME,path),path)
    url=urlparse.urljoin(URL_BASE,path)
    print '%6s:%s' %(parser.can_fetch(AGENT_NAME,url),url)
    print

