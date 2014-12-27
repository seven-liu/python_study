#encoding:utf-8

import SimpleAsyncHTTP
import asyncore

class DummyConsumer:
    size=0

    def http_header(sefl,request):
        if request.status is None:
            print "connnection failed"
        else:
            print "status","=>",request.status
            for key, value in request.header.items():
                print key,"=",value

    def feed(self,data):
        self.size=self.size+len(data)

    def close(self):
        print self.size+"bytes in body"

consumer=DummyConsumer()
request=SimpleAsyncHTTP.AsyncHTTP(
      "http://www.pythonware.com",
      consumer
       )
asyncore.loop()
