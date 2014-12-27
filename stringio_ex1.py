#encoding:utf-8

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO


def _write2Buff():
    output=StringIO()
    output.write('This goes into the buffer.')
    print >>output,'And so does this.'

    print output.getvalue()

    output.close()

    input=StringIO('Inital value for read buffer.')
    print input.read()

_write2Buff()