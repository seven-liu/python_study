#encoding:utf-8

#from codecs_to_hex import to_hex
import binascii
import codecs


def encoded_decodeds(file):
    encoded=file.encode('utf-8')
    decoded=encoded.decode('utf-8')
    print 'original : ',repr(file)
    print 'Encoded : ',to_hex(encoded,1),type(encoded)
    print 'Decoded : ',repr(decoded),type(decoded)

Mylist=['a','2.03']
for item in Mylist:
    encoded_decodeds(item)