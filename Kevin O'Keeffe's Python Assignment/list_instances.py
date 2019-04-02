#!/usr/bin/env python3
# Richard Frizby Moodle Notes 
import boto3
ec2 = boto3.resource('ec2')
#Lists all instances
def list_instances():
    for instance in ec2.instances.all():
      for tag in instance.tags:
          print ('')
          print (' Name: ', tag['Value'],'\n ID:   ',instance.id,'\n State:',instance.state['Name'],'\n I.P:  ',instance.public_ip_address)
          print ('')

#Calling function
def main():
    list_instances()

if __name__ == '__main__':
    main()
