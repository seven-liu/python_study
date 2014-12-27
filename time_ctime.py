#encoding utf-8

import time

print 'time is:', time.ctime()
later=time.time()+15
print '15 secs later:',time.ctime(later)
print time.ctime(), '%0.3f %0.3f' %(time.time(),time.clock())


