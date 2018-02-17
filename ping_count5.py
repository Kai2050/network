import time as t
import datetime
import os


def ping():
    hostname = "10.0.0.17"
    response = os.system("ping -c 3 " + hostname)

def sweep():
        number=0
        start_time = datetime.datetime.now()
        start_clock = start_time.strftime("%H:%M:%S")
        print('Scan started at %s' % start_clock)

        while True:                
                #print('Sweep started, number is %s' % int(number))   
                hostname = "10.0.0.17"
                response = os.system("ping -c 3 " + hostname)
                if response != 0: # no host found
                    start_time_false = t.time()
                    #false_start_clock = datetime.datetime.now
                    print('Stage 1 - No host found')
                    t.sleep(5)

                    while True:
                        hostname = "10.0.0.16"
                        response = os.system("ping -c 3 " + hostname)
                        response != 0 # no host found

                        time_elapsed = t.time() - start_time_false
                        #elapsed_clock = (time_elapsed.strftime("%H:%M:%S")) # show elapsed time with normal clock
                        elapsed_clock = t.strftime("%H:%M:%S", t.gmtime(time_elapsed))
                        print('Stage 2 - count is STILL: %s' % int(number) + ' after %s ' % elapsed_clock )
                        t.sleep(5)        

                        if time_elapsed >= 1800:
                            print('Stage 3 - host has been out for 15 minutes, checking for return...')
                            t.sleep(5)
                        
                            if response == 0: # host found
                                number = number+1                     
                            
                                time_elapsed = t.time() - start_time_false
                                elapsed_clock = t.strftime("%H:%M:%S", t.gmtime(time_elapsed)) # show elapsed time with normal clock
                                return_time = datetime.datetime.now()
                                return_clock = return_time.strftime("%H:%M:%S")
                                print('Stage 4 - number up by 1 - after no host')
                                print('count is NOW %s' % int(number) + ' after %s ' % elapsed_clock )                            
                                print('******************************************************* ')
                                print('Host found after being out for %s ' % elapsed_clock)
                                print('Host arrived back at ' % return_clock)
                                print('******************************************************* ')
                                print('Resetting counter...')
                                print('******************************************************* ')
                                number = 0
                                t.sleep(300)
                                

                        if response == 0: # host found
                                number = number+1
                            
                                t.sleep(300)
                        
                
                if response == 0: # host found
                    number = number+1          
                    print('Host found, number up by 1,' + ' count is %s' % number)
                    t.sleep(5)


sweep()
