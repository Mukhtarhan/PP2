import datetime
x = datetime.datetime(2013,12,30,23,59,59)
y = datetime.datetime(2013,12,31,23,59,59)
print((y-x).total_seconds())
