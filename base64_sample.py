#encoding: utf-8

import base64

Message="life is beatiful"

#file=open("out.txt","w")
#file.write(message)
#file.close()

data=base64.encodestring(Message)
original_data=base64.decodestring(data)


#base64.encode(open("out.txt"),open("out.b64","w"))
#base64.decode(open("out.b64"),open("out.txt","w"))

print "original:",repr(Message)
#print "encoded message:",repr(open("out.b64").read())
#print "decoded message:",repr(open("out.txt").read())

print "encoded data:",repr(data)
print "decoded data:",repr(original_data)
