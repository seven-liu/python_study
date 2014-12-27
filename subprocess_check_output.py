#encoding:utf-8

import subprocess

output=subprocess.check_output(['dir'])
print 'Have %d bytes in output' %len(output)
print output


