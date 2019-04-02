#!/usr/bin/env python3
import sys
import boto3
import time
import os
import subprocess
ec2 = boto3.resource('ec2')

#Function to terminate instances
def kill():
  loop = True
  #Subprocess call list instances function
  subprocess.call(['python3','list_instances.py'])

  #while loop
  while loop:

    try:
      #Input ID of instance to terminate
      instancename = input('Please enter I.D. of instance to terminate:')
      #Check to see if the instance name has content
      if instancename is not None:
        instance = ec2.Instance(instancename)
        responce = instance.terminate()
        time.sleep(.2)
        print ("Instance Terminated")
        time.sleep(.2)
        print('')
        exit()
        return
        
    #Exception to ask for a valid id
    except Exception:
      #If instance name is = to exit closes loop and opens up main menu
      if instancename == 'exit':
        loop=False
        subprocess.call(['python3','home_menu.py'])
        exit()
        return
      #If the var instance name has no valid contents the user is promped to give one.
      #The loop continues
      time.sleep(.5)
      print('Please enter a valid I.D. or type exit to quit')
      time.sleep(.5)


def main():
    kill()
    loop = False
    os.system('clear')
    exit()

if __name__ == '__main__':
    main()
