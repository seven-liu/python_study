#encoding:utf-8

import smtplib

server=smtplib.SMTP('mail')
server.set_debuglevel(True)
try:
   dhellmann_result=server.verify('dellmann')
   notthere_result=server.verify('nothere')
finally:
    sever.quit()

print 'dhellmann:',dehellmann_result
print 'notthere:',notthere_result
