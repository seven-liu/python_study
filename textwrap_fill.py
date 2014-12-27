#encoding:utf-8

import textwrap

sample_text='''
  The textwrep module can be used to format text output in
  situations where pretty-printing is desired. It offers
  programmatic functionality similar to the paragraph wrapping
  or filling features found in many texst editors.
'''

dedented_text=textwrap.dedent(sample_text)

print 'Dedented:'
print dedented_text

#print 'No dedent:\n'
#print textwrap.fill(sample_text,width=50)