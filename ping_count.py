import time
import datetime
import os

def ping(): # 1 hour cycle
    time_start = time.time()
    number = 0
    while True:
        #print('Scan started at %s ') % time_start
        hostname = "10.0.0.17"
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            number = number +1
            print('Count increase by 1. Scanning again in 5 minutes ***')
        #else:
#            print('No host found...checking if blip')

        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(number)
        time_elapsed = time.time() - time_start
        print(time_elapsed)
        print(time.strftime("%H:%M:%S", time.gmtime(time_elapsed)))

        if time_elapsed > 1200 and (number == 0):
            print('...checking again')
            response = os.system("ping -c 1 " + hostname)
            if response != 0:
                print('flash lights')
            
        time.sleep(300)
        

        
for i in range(5):
    
        ping()
#        time.sleep(1)
