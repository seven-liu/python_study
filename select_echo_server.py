#encoding:utf-8

import select
import socket
import sys
import Queue

#create TCP/IP socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)

#bind the socket to the port
server_address=('localhost',10000)
print >>sys.stderr,'starting up on %s port %s' %server_address
server.bind(server_address)

#listen for coming connection
server.listen(5)

#socket from which we expect to read
inputs=[server]

#socket to which we expect to write
outputs=[]

message_queues=[]

while inputs:
    print >>sys.stderr,'waiting for the next event'
    readable,writable,exceptional=select.select(inputs,outputs,inputs)



#handle inputs
    for s in readable:
      if s is server:
        connection,client_address=s.accept()
        print >>sys.stderr,'connection from',client_address
        connection.setblocking(0)
        inputs.append(connection)

        message_queues[connection]=Queue.Queue()

      else:
         data=s.recv(1024)
         if data:
            print >>sys.stderr,'received "%s" from %s' %(data,s.getpeername())
            message_queues[s].put(data)
            if s not in outputs:
                outputs.append(s)

         else:
            print >>sys.stderr,'closing',client_address
            if s in outputs:
                outputs.remove(s)
                s.close()
                del  message_queues[s]

#handle outputs
    for s  in writable:
      try:
        next_msg=message_queues[s].get_nowait()
      except Queue.Empty:
        print >>sys.stderr,'',s.getpeername(),'queue empty'
        outputs.remove(s)
      else:
        print >>sys.stderr,'sending "%s" to %s' %(next_msg,s.getpeername())
        s.send(next_msg)

#handle exceptions
    for s in exceptional:
      print >>sys.stderr,'exception condition on',s.getpeername()
      inputs.remove(s)
      if s in outputs:
        outputs.remove(s)
      s.close()
      del message_queues[s]


