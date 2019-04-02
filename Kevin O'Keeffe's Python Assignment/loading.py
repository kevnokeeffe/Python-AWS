#!/usr/bin/env python3

#Ref1 https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
#Ref2 https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method

import boto3
import sys, time, threading

# Define the process.
def the_process_function():
    #set var for time
    n = 120
    for i in range(n):
        time.sleep(1)
        sys.stdout.write('\r'+'loading...  process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')

        #"flush" the buffer
        sys.stdout.flush()
    sys.stdout.write('\r'+'loading... finished               \n')
    print('')

#Animated loading bars
def animated_loading():
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush()

the_process = threading.Thread(name='process', target=the_process_function)

the_process.start()

while the_process.isAlive():
    animated_loading()
