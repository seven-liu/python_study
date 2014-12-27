#encoding:utf-8

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass


#prompt the user for connection info
to_email=raw_input('Recipient:')
servername=raw_input('Mail server name:')
username=raw_input('Mail username:')
password=getpass.getpass("%s's password:" %username)


#create message

msg=MIMEText('This is the body of message.')
msg.set_unixfrom('author')
msg['To']=email.Utils.formataddr(('Recipient',to_email))
msg['From']=email.utils.formataddr(('Author','author@example.com'))
msg['Subject']='simple test message'

server=smtplib.SMTP(servername)
#show communication with the server
try:
    server.set_debuglevel(True)
    if server.has_extn('STARTTLS'):
        server.starttls()
        server.ehlo()
    server.login(username,password)
    server.sendmail('author@example.com',[to_email],msg.as_string())

#try:
#    server.sendemail('author@example.com',
#                     ['recipient@example.com'],
#                    msg.as_string())


finally:
    server.quit()

