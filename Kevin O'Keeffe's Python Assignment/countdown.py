#!/usr/bin/env python3

import time
import sys

def countdown():
    c=':'
    #Declare variables
    secz= 15
    print('')


    sec=int(secz)
    #While loop that runs through the countdown

    while sec > 0:
        sec=sec-1
        time.sleep(1)
        sec1 = ('%02.f' % sec)  # format
        sys.stdout.write('\r'+'Loading...' + str(sec1))
    sec=60
    print('')
    print('Fully Loaded.')
    time.sleep(1)
    print('')
    time.sleep(1)

def main():
    countdown()

if __name__ == '__main__':
    main()
