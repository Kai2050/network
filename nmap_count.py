#!/usr/bin/env python
#python2

import nmap
import time
import datetime
from picamera import PiCamera

camera = PiCamera()
camera.rotation = 180
camera.led = False
camera.framerate = 25
camera.resolution = (960, 540)
save_dir = "/home/pi/vid/"
time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def video_5min():
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def get_file_name():
      return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    filename = "%s%s" % (save_dir, get_file_name())
    print("Starting to record 5 minutes at %s" % (time_now))
    camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.start_preview()
    camera.start_recording(filename)
    time.sleep(300)
    camera.stop_recording()
    camera.stop_preview()
    print("Finished recording @ %s" % (time_now))

nm = nmap.PortScanner()
nm.scan(hosts='10.0.0.8', arguments='-sP -n -PE -PA21,23,80,3389')

def sweep():
        print('----------------------------------------------------')
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Scan started at %s ') % time_now
        for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                if nm[host].state()=='up':
                        count+=1
                        print('OG is in, counted up by 1')
        time.sleep(0.1)

def block():
        count=0
        for i in range(5):
                time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                sweep()
                
                if count > 0:
                        print('count is %s, OG is in' % count)
                        time.sleep(300)
                else:
                        print('OG is out')
                        video_5min()
                time.sleep(0.2)
for i in range(12): #loop for 1 hours
        block()
        time.sleep(0.2)


time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('Scan finished at %s ') % time_now
