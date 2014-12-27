#encoding: utf-8
import threading
import Queue
import time,random
import os
import sys


WORKERS=2

class Worker(threading.Thread):
    def __init__(self,queue):
        self.__queue=queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            item=self.__queue.get()
            if item is None:
                break
            time.sleep(random.randint(10,100)/1000.0)
            print "task",item,"finished"

queue=Queue.Queue(3)

for i in range(WORKERS):
    Worker(queue).start()

for item in range(10):
    print "push",item
    queue.put(item)


for i in range(WORKERS):
    queue.put(None)
