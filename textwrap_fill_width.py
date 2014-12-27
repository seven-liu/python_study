#encoding:utf-8

import textwrap
from textwrap_fill import sample_text

dedented_text=textwrap.dedent(sample_text).strip()

for width in [50,75]:
    print '%d Columns:\n' %width
    print textwrap.fill(dedented_text,width=width)
    print
