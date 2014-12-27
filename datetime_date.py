#encoding:utf-8

import datetime

def time_struct(s):
    print 'tuple : tm_year =', s.tm_year
    print '   tm_mon =',s.tm_mon
    print '   tm_mday =',s.tm_mday
    print '   tm_hour =',s.tm_hour
    print '   tm_min =',s.tm_min
    print '   tm_sec =',s.tm_sec
    print '   tm_wday =',s.tm_wday
    print '   tm_yday =',s.tm_yday
    print '   tm_isdst =',s.tm_isdst

def today_struct(t):
    print 'Original: ',t.toordinal()
    print '   Year: ',t.year
    print '   Mon: ',t.month
    print '   Day: ',t.day

today=datetime.date.today()
print today
today_struct(today)

print 'ctime :',today.ctime()
tt=today.timetuple()
time_struct(tt)
