#!/usr/bin/env python3
import sys
import boto3
import time
s3 = boto3.resource("s3")

def create_bucket():
    print ('\nCreating a new bucket')
    time.sleep(1)
    bucket_name = input('Please give your new bucket a unique name: ')
    time.sleep(1)
    try:
         response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
         time.sleep(1)
         print ('\nA new bucket has been created')
         print (response)

    except Exception as error:
         print (error)
         print('Please try again')

 

def main():
    create_bucket()
    time.sleep(2)

if __name__ == '__main__':
    main()
