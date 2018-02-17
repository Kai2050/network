import time as t
import datetime
import os

hostname = "10.0.0.16"

def sweep():
        number=0
        start_time = datetime.datetime.now()
        start_clock = start_time.strftime("%H:%M:%S")
        print('Scan started at %s' % start_clock)

        while True:                
                #print('Sweep started, number is %s' % int(number))   
                #hostname = "10.0.0.17"
                response = os.system("ping -c 3 " + hostname)
                if response != 0: # no host found
                    start_time_false = t.time()
                    start_time_clock = datetime.datetime.now()
                    false_start_clock = start_time_clock.strftime("%H:%M:%S")
                    print('Stage 1 - No host found at %s' % false_start_clock)
                    t.sleep(300) #sleep

                    while True:
                        #hostname = "10.0.0.16"
                        response = os.system("ping -c 3 " + hostname)
                        if response != 0: # no host found

                            time_elapsed = t.time() - start_time_false
                            #elapsed_clock = (time_elapsed.strftime("%H:%M:%S")) # show elapsed time with normal clock
                            elapsed_clock = t.strftime("%H:%M:%S", t.gmtime(time_elapsed))
                            print('Stage 2 - count is STILL %s' % int(number) + ' after %s ' % elapsed_clock )

                            t.sleep(300) #sleep       

                            if time_elapsed >= 3600:
                                print('Stage 3 - host has been out for 30 minutes or more, checking for return...')
                                
                                t.sleep(300) #sleep
                                #hostname = "10.0.0.16"
                                response = os.system("ping -c 3 " + hostname)
                                
                                
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
                                    print('Host arrived back at %s' % return_clock)
                                    print('******************************************************* ')
                                    print('Resetting counter...')
                                    print('******************************************************* ')
                                    number = 0
                                    t.sleep(300) #sleep
                                    break
                                    

                        if response == 0: # host found
                                number = number+1
                            
                                t.sleep(300) #sleep
                        
                
                if response == 0: # host found
                    number = number+1          
                    print('Host found, number up by 1,' + ' count is %s' % number)
                    t.sleep(300)


sweep()
