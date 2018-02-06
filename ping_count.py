import time
import datetime
import os

def ping():
    time_start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    count = 0
        for i in range(12):
            print('Scan started at %s ') % time_now
            hostname = "10.0.0.16"
            response = os.system("ping -c 3 " + hostname)
            if response == 0:
                count=+1
                print('Count increase by 1. Scanning again in 5 minutes ***') #hostname, 'is up!'
            else:
                print('No host found')
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if (current_time - time_start) > 1 and count = 0
                response = os.system("ping -c 3 " + hostname)
                if response == 0:
                    print ('success')
            time.sleep(300)

while True:
        ping()
        time.sleep(1)
