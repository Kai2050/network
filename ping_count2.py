import time
import datetime
import os

def ping(): # 2 hour cycle

    time_start = time.time()
    number = 0
    for i in range(144):
        print('- - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - ')
        print('Scan started') # at %s ') % time_start
        hostname = "10.0.0.16"
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            number = number +1
            print('count is %s' % int(number))
            
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time_elapsed = time.time() - time_start        
        elapsed_clock = (time.strftime("%H:%M:%S", time.gmtime(time_elapsed)))
        print(elapsed_clock)
        print('count is %s' % int(number))

        if time_elapsed > 1800 and (number == 1):
            print(' ')
            print('******************************************************* ')
            print('Host found after %s' % elapsed_clock)
            print('*******************************************************')
            print(' ')
            number = 0
            time_start = time.time()
        time.sleep(300)
        print('- - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - ')
                            
for i in range(5):
    
        ping()
#        time.sleep(1)
