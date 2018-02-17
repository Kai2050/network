import time as t
import datetime

time = t.time()
date  = datetime.datetime.now()

print(time)
print(date)

now = datetime.datetime.now()
print(now)
print (now.strftime("%H:%M:%S"))
t.sleep(10)

date_two = datetime.datetime.now()

time_elapsed = date_two - date
print(time_elapsed)
if time_elapsed > 20:
    print('more than 20')
else:
    print('less than 20')
