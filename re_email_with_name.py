#encoding:utf-8

import re

address=re.compile(
  '''
   ((?P<name>
     ([\w.,]+\s+)*[\w.,]+)
     \s*
     <
   )?

   (?P<email>
    [\w\d.+-]+
    @
    ([\w\d.]+\.)+
    (com|org|edu|cn)
   )

   >?
  ''',
  re.UNICODE|re.VERBOSE)

candidates=[
  u'first.last@example.com',
  u'first.last+category@gmail.com',
  u'valid-address@mail.example.com',
  u'not-valid@example.foo',
  u'first LAST <firs.last@example.com>',
  u'No Brackets first.last@example.com',
  u'first.last',
  u'first middle last<firs.last@example.com>',
  u'first M.last<first.last@example.com>',
  u'<first.last@example.com>',
   ]

for candidate in candidates:
    print 'Candidate: ',candidate
    match=address.search(candidate)
    if match:
        print ' Name:',match.groupdict()['name']
        print ' Email:',match.groupdict()['email']
    else:
        print ' No match'



