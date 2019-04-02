#!/usr/bin/env python3
import boto3
import time

s3 = boto3.resource('s3')

def list_bucket():
    try:
        for bucket in s3.buckets.all():
         print (bucket.name)
         print ("---")
        for item in bucket.objects.all():
         print ("\t%s" % item.key)

    except Exception:
        print('No Buckets to Display')

def main():
    list_bucket()

if __name__ == '__main__':
    main()
   
