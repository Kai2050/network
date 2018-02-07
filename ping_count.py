import time
import datetime
import os

def ping(): # 1 hour cycle
    time_start = time.time()
    number = 0
    while True:
        number = 0
        print('- - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - ')
        print('Scan started') # at %s ') % time_start
        hostname = "10.0.0.17"
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            number = number +1
            print('count is %s' % int(number))

        time.sleep(300)

        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time_elapsed = time.time() - time_start        
        elapsed_clock = (time.strftime("%H:%M:%S", time.gmtime(time_elapsed)))
        print(elapsed_clock)

        if number == 0:
            print('host not found, count stays at 0')
        if time_elapsed > 1800 and (number == 0):
            print('No response for %s') % elapsed_clock + (' checking again')
            print('waiting for 60 seconds')
            time.sleep(60)            
            response = os.system("ping -c 1 " + hostname)
            if response == 0:
                print('Host found after %s' % elapsed_clock)
            
        #time.sleep(60)
        

        
for i in range(5):
    
        ping()
#        time.sleep(1)
