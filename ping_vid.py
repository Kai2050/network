#!/usr/bin/env python
#python2

import time
import datetime
from picamera import PiCamera
import os

camera = PiCamera()
camera.rotation = 180
camera.led = False
camera.framerate = 25
camera.resolution = (960, 540)
save_dir = "/home/pi/vid/"

#Record 5 minuts of video

#def video_5min():
#    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    def get_file_name():
#      return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
#    filename = "%s%s" % (save_dir, get_file_name())
#    print("*** OG is out, starting to record 5 minutes at %s ***" % (time_now))
#    camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    camera.start_preview()
#    camera.start_recording(filename)
#    time.sleep(300)
#    camera.stop_recording()
#    camera.stop_preview()
#    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    print("Finished recording @ %s" % (time_now))

def video_5min():
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start = datetime.datetime.now()
    def get_file_name():
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    filename = "%s%s" % (save_dir, get_file_name())
    print("*** OG is out, starting to record 5 minutes at %s ***" % (time_now))
    camera.start_preview()
    camera.start_recording(filename)
    while (datetime.datetime.now() - start).seconds < 300:
        camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.wait_recording(0.2)
    camera.stop_recording()
    camera.stop_preview()
    print("Finished recording @ %s" % (time_now))

#Ping hostname

def ping():
        print('----------------------------------------------------')
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Scan started at %s ') % time_now
        hostname = "10.0.0.8" #example
        response = os.system("ping -c 3 " + hostname)
        if response == 0:
            print(' ')
            time.sleep(1)
            print('*** OG is in. Scanning again in 3 minutes ***') #hostname, 'is up!'
            time.sleep(300)
        else:
            print(' ')
            #print('OG is out, starting to record 5 minutes of video')
            video_5min()

for i in range(36): #loop for 1 hour
        ping()
        time.sleep(1)


time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('Scan finished at %s ') % time_now
