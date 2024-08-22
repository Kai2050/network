#!/usr/bin/env python

import os
import time
import datetime

def ping():
  time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  hostname = "10.0.0.16" #example
  print()
  response = os.system("ping -c 2 " + hostname)

#and then check the response...
  if response == 0:
    print()
    print ('- - - - - - - - - - - - - - - - - - - - - - - - - - ')
    print (hostname, 'is up @ %s !' % time_now)
    
  else:
    print()
    print ('- - - - - - - - - - - - - - - - - - - - - - - - - - ')
    print (hostname, 'is down @ %s !' % time_now)
    
for i in range(60):
  ping()
  time.sleep(300)
  
