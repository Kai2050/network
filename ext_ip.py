#!/usr/bin/env python
#python2


    start = datetime.datetime.now()
    def get_file_name():
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    filename = "%s%s" % (save_dir, get_file_name())
    print("*** OG is out, starting to record 5 minutes at %s ***" % (time_now))



import urllib
import re
import datetime

time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_external_ip():
    site = urllib.urlopen("http://checkip.dyndns.org/").read()
    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
    address = grab[0]
    return address

if __name__ == '__main__':
    print( get_external_ip() + time_now )
