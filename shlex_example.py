#encoding:utf-8
import shlex
import sys

if len(sys.argv)!=2:
    print "please specify one filename on the command line."
    sys.exit(1)

filename=sys.argv[1]
body=file(filename,'rt').read()
print 'ORIGINAL:',repr(body)
print

print 'TOKENS:'
lexer=shlex.shlex(body)
for token in lexer:
    print repr(token)
