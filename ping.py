#!

import os
import time
import datetime

def ping():
  time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  hostname = "10.0.0.16" #example
  response = os.system("ping -c 1 " + hostname)

#and then check the response...
  if response == 0:
    print hostname, 'is up @ %s !' % time_now
  else:
    print hostname, 'is down @ %s !' % time_now

for i in range(10):
  ping()
  time.sleep(300)
