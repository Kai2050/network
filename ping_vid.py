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

#Record 5 minuts of video

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
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Finished recording @ %s" % (time_now))


nm = nmap.PortScanner()

def sweep():
        count=0
        print('----------------------------------------------------')
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        nm.scan(hosts='10.0.0.8', arguments='-sP -n -PE -PA21,23,80,3389')
        print('Scan started at %s ') % time_now
        for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                if nm[host].state()=='up':
                        count+=1
                        print('OG is in, counted up by 1')
        if count > 0:
                print('Count is %s, OG is in. Scanning again in 3 minutes' % count)
                time.sleep(180)
        else:
                print('OG is out')
                video_5min()

for i in range(36): #loop for 1 hour
        sweep()
        time.sleep(1)


time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('Scan finished at %s ') % time_now
