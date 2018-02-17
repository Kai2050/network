import time
import datetime
import os

def ping(): # 1 hour cycle

    time_start = time.time()
    number = 0

    while True:
        number = start_number
        time_elapsed = time.time() - time_start        
        elapsed_clock = (time.strftime("%H:%M:%S", time.gmtime(time_elapsed)))

        print('count is %s' % int(number) + ' after %s ' % elapsed_clock )
        print('- - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - ')
        #print('Scan started') # at %s ') % time_start
        hostname = "10.0.0.16"
        response = os.system("ping -c 1 " + hostname)
        if response == 0: 
            number = number +1 
            last_countup = number # register new number total after host found
            countup_time = time.time() # register time when last host was found

            time_elapsed = time_start - countup_time # time elapsed from start to last time host found     
            elapsed_clock = (time.strftime("%H:%M:%S", time.gmtime(time_elapsed))) # show elapsed time with normal clock

            if time_elapsed > 900 and (number == last_countup): # check if in last 15 minutes number has stayed the same?
                print('count is %s' % int(last_countup) + ' after %s ' % elapsed_clock )
                print(' ')
                print('******************************************************* ')
                print('Host found after %s' % elapsed_clock)
                print('*******************************************************')
                print(' ')
                number = 0 # reset number counter to zero to start again as host was found
                time_start = time.time()
        time.sleep(300)
        print('- - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - ')
                            
for i in range(1):
    ping()
        
