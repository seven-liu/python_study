#encoding:utf-8

import re

def test_patterns(text,patterns=[]):
    for pattern,desc in patterns:
        print 'Pattern %r (%s)\n' %(pattern,desc)
        print ' %r' %text
        for match in re.finditer(pattern,desc):
            s=match.start()
            e=match.end()
            substr=text[s:e]
            n_backslashes=text[:s].count('\\')
            prefix='.'*(s+n_backslashes)
            print ' %s%r' %(prefix,substr)
        print
    return

test_patterns(
 'abbaabbba',
 [('ab*', 'a followed by zero or more b'),
  ('ab+', 'a followed by one or more b'),
  ('ab?', 'a followed by zero or one b'),
  ('ab{3}', 'a followed by three b'),
  ('ab{2,3}', 'a followed by two or three b'),
  ('[ab]+', 'a or b'),
  ('a[ab]+', 'a followed by 1 or mor a or b'),
  ('a[ab]+"}', 'a followed by 1 or mor a or b, not greedy'),

  ])

