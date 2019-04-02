#!/usr/bin/env python3
import sys
import boto3
import subprocess
s3 = boto3.resource('s3')
import time
import os

#Declaring loop in function
def delbuck():
  loop = True
  return loop

#Main function to check s3 list of buckets takes input and deletes selected bucket and contents
def del_loop(loop):

  #Try catch to list the buckets
  try:
      for bucket in s3.buckets.all():
       print (bucket.name)
       print ("---")
      for item in bucket.objects.all():
       print ("\t%s" % item.key)

     #While loop looking for valid input
      while loop:
        try:
          bucketname = input('Please enter name of bucket to delete: ')
          print('')
          bucket = s3.Bucket(bucketname)
          #if statement looking for the input exit to quit the function/subprocess
          if bucketname == 'exit':
            loop = False
            os.system('clear')
            #subprocess opens the home menu
            subprocess.call(['python3','home_menu.py'])
          #if the s3 bucket list is not empty delete the inputed bucket
          elif bucket is not None:
               for key in bucket.objects.all():
                   try:
                       response = key.delete()
                       print ('Contents Deleted')
                   except Exception as error:
                       print ('No Contents to Delete')
               response = bucket.delete(bucketname)
               print ('Bucket Deleted')
               loop = False
               input('Press enter to return to menu.')
        #exception print out looking for valid bucket name
        except Exception:
            print('Please enter a valed bucket name!\nType exit to stop')
            print('')
  #If the s3 bucket list is empty this except will kick into play
  except Exception:
      print('No Buckets to Display')
      input('Press enter to return to menu.')

#Call functions
def main():
    loop = delbuck()
    del_loop(loop)

if __name__ == '__main__':
    main()
