#!/usr/bin/env python
#python2

import nmap
import time
import datetime

nm = nmap.PortScanner()

nm.scan(hosts='10.0.0.8', arguments='-sP -n -PE -PA21,23,80,3389')



def sweep():
        print('----------------------------------------------------')
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Scan started at %s ') % time_now 
        for host in nm.all_hosts():                       
                #print('Host : %s (%s)' % (host, nm[host].hostname()))
                #print('State : %s' % nm[host].state())

                if nm[host].state()=='up':
                        count+=1
                        print('Counted up 1')
                #elif nm[host].state()!='up':                
		#	print('OG is out')
                
        time.sleep(0.1)
        
def block():
        count=0
        for i in range(5):
                time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                sweep()
                #count+=1
                if count > 3:
                        print('count is %s, OG is in' % count)
                else:
                        print('OG is out')

                time.sleep(180)
for i in range(8): #loop for 2 hours
        block()
        time.sleep(0.2)


time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('Scan finished at %s ') % time_now	

