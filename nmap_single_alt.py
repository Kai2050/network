#!/usr/bin/env python
#python2

import nmap
import time
import datetime

nm = nmap.PortScanner()

print('                                                    ')
time.sleep(1)
print('----------------------------------------------------')
how_long = raw_input(int('How many minutes do you want to scan for? '))
repeat = how_long*2 #because 2 sweeps per minute

time.sleep(1)

def sweep():
	nm.scan(hosts='10.0.0.8', arguments='-n -sP -PE -PA21,23,80,3389')
	hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
	for host, status in hosts_list:
	    print('{0}:{1} '.format(host, status)) + '@ ' + (  datetime.datetime.now().strftime("%H:%M:%S"))
for i in range(5):
	sweep()
	time.sleep(28)
