#encoding:utf-8

import imaplib
import ConfigParser
import os

def open_connection(verbose=False):
    #read the config file
    config=ConfigParser.ConfigParser()
    config.read([os.path.expanduser('~/.pymotw')])

    #connect to the server
    hostname=config.get('server','hostname')
    if verbose:print 'Connecting to',hostname
    connection=imaplib.IMAP4_SSL(hostname)

    #login to our account
    username=config.get('account','usrname')
    password=config.get('account','usrname')
    if verbose:print'Logging in as',username
    connection.login(username,password)
    return connection

if __name__=='__main__':
    c=open_connection(verbose=True)
    try:
       print c
    finally:
        c.logout()

