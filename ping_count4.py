import time
import os


def ping():
    hostname = "10.0.0.17"
    response = os.system("ping -c 3 " + hostname)

def sweep():
        number=0
        start_time = time.time

        while True:                
                print('Sweep started, number is %s' % int(number))   
                hostname = "10.0.0.17"
                response = os.system("ping -c 3 " + hostname)
                if response != 0: # no host found
                    start_time_false = time.time()
                    number_false = number
                    print('No host found')
                    time.sleep(5)
                    

                    while True:
                        hostname = "10.0.0.17"
                        response = os.system("ping -c 3 " + hostname)
                        response != 0 # no host found

                        time_elapsed = time.time() - start_time_false
                        elapsed_clock = (time.strftime("%H:%M:%S", time.gmtime(time_elapsed))) # show elapsed time with normal clock
                        print('count is STILL: %s' % int(number) + ' after %s ' % elapsed_clock )

                        if time_elapsed >= 120:
                            print('host has been out for 2 minutes, checking for return...')
                        time.sleep(5)
                        
                        if response == 0: # host found
                            number = number+1                     
                        
                            time_elapsed = time.time() - start_time_false
                            elapsed_clock = (time.strftime("%H:%M:%S", time.gmtime(time_elapsed))) # show elapsed time with normal clock
                            print('number up by 1 - after no host')
                            print('count is NOW %s' % int(number) + ' after %s ' % elapsed_clock )

                            if (number == number_false +1) and (time_elapsed) >= 120:
                                print('******************************************************* ')
                                print('Host found after being out for %s ' % elapsed_clock)
                                print('******************************************************* ')
                                print('Resetting counter...')
                                print('******************************************************* ')
                                number = 0
                                time.sleep(5)
                                break
                        
                else:
                    ping()
                    number = number+1          
                    print('Number up by 1 (straight to else)' + ' count is %s' % number)
                    time.sleep(10)


sweep()
