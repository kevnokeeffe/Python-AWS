#!/usr/bin/env python3
import os
import boto3
import subprocess
import time
import webbrowser
from subprocess import *

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

def bucket_select():
    #Call subprocess list buckets
    subprocess.call(['python3','list_buckets.py'])
    try:
      #enter bucket name
      buckets = input('\nPlease type in the name of the bucket you wish to choose a file from: ')
      #for loop looking through buckets
      for bucket in s3.buckets.all():
        #if statement checking if the input is the same as a bucket name
        if buckets == bucket.name:
          #enter file name from bucket
          url = input('\nPlease type in the name of the file you wish to copy to the Index page: ')
          #search through bucket objects to check if the input is matching a file
          for item in bucket.objects.all():
            #if it does match do this
            if url == item.key:
              file_url = "https://s3-eu-west-1.amazonaws.com/" + buckets + "/" + url
              index = open("index.html", "w")
              img_tag = "<img src='{}'>".format(file_url)
              index.write(img_tag)
              index.close()
              print('working')
              instance_create()
              return
          if url != item.key:
            print('Enter valid details')
            bucket_select()
      if buckets != bucket.name:
        print('Please enter valid name')
        bucket_select()
      return buckets
    except Exception:
      print('Error!')

def instance_create():
    try:
        #Lists instances
        subprocess.call(['python3','list_instances.py'])
        #ask for input ip address of instance
        ip = input('\nPlease type in the I.P. of the instance you wish to upload to: ')
        for instance in ec2.instances.all():
          for tag in instance.tags:
            #if the ip matches an instance ip add it to the index
            if ip == instance.public_ip_address:
              touch_index = 'ssh -i assignment_key.pem ec2-user@'+ip+' sudo touch /var/www/html/index.html'
              change_permissions = 'ssh -i assignment_key.pem ec2-user@'+ip+' sudo chmod 777 /var/www/html/index.html'
              scp_index = 'scp -i assignment_key.pem index.html ec2-user@'+ip+':/var/www/html/'
              run(touch_index, check=True, shell=True)
              run(change_permissions, check=True, shell=True)
              run(scp_index, check=True, shell=True)
              time.sleep(.2)
              print('Web browser loading..')
              time.sleep(.2)
              print('Exit webbrowser to return to menu')
              time.sleep(.2)
              #launch web brouser
              subprocess.run("firefox "+ip, shell=True)
              return
        if ip != instance.public_ip_address:
            print('Enter valid I.P. address!')
            time.sleep(1)
            instance_create()

    except Exception:
           print('Enter Valid Details!')

# Define a main() function
def main():
    bucket_select()
    input('Press enter for menu')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
