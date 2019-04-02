#!/usr/bin/env python3
# Ref1: https://medium.com/@kiamatthews/using-python-to-add-rules-to-an-aws-security-group-ee56def5bf78
#Ref2:https://cloudarchitect.net/articles/159
import boto3
from subprocess import *
import time
import os
import sys
import subprocess
from botocore.exceptions import ClientError

#declare ecTwo client variable
ecTwo = boto3.client('ec2')
#declare s3 variable
s3 = boto3.resource("s3")
#declare ec2 resource variable
ec2 = boto3.resource('ec2')

#Creating security group..
def security_group():
    
    try:
        response = ecTwo.describe_vpcs()
        #Getting vpc id
        vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
        #Asking user for Group Name and Description
        response = ecTwo.create_security_group(GroupName= input('Please give your security group a name: '),
                                             Description= input('Please give your security group a description: '),
                                             VpcId= vpc_id)
        security_group_id = response['GroupId']
        print(' Security Group Created. \n Group ID: '+ security_group_id + '\n VPC ID: ' + vpc_id)
        data = ecTwo.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])

        print('')
        sec1 = security_group_id
        print('')
        print(' Security Group Created')
        time.sleep(1.5)
        return sec1
    except CalledProcessError:
           print('Error 404!!')
           print('Try again!!')

def create_instance(sec1):
    #Give your instance a name
    instancename = input('Please give your new instance a name: ')
    tags = [{'Key': 'Name', 'Value': instancename}]
    tag_spec = [{'ResourceType': 'instance', 'Tags': tags}]

    #Create the instance, httpd apache server, install python, security group(created earlier), and key.
    try:
        instance = ec2.create_instances(
        ImageId = 'ami-0fad7378adf284ce0',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro',
        KeyName = 'assignment_key',
        TagSpecifications = tag_spec,
        SecurityGroupIds = [sec1],
	UserData ="""#!/bin/bash
		  yum update -y
		  yum install httpd -y
		  yum install Python36
                  yum install pip3 -qq
		  systemctl enable httpd
                  systemctl start httpd"""
	)


        print ("An EC2 instance with ID", instance[0].id, "has been created.")
        #Waites untill instance is running
        time.sleep(.5)
        #Loads subprocess loading.py which animates the loading process
        subprocess.call(['python3', 'loading.py'])
        time.sleep(1)
        print ("Instance is running.")
        time.sleep(1)
	#Reloads the instance
        instance[0].reload()
	#Captures the dns in a string called ip
        ip = instance[0].public_dns_name
        print ('I.P. address:'+ip)	
	#returns the ip
        return ip

    except Exception as error:
        print ('Error!')
        print (error)

def check_web(ip):
    try:
       #Calling countdown subprocess
       print ("IP: "+ip)
       print ("")
       print ("Installing Python..")
       time.sleep(1)
       #Installing python 3 on server
       ssh_install_python = 'ssh -t -o StrictHostKeyChecking=no -i assignment_key.pem ec2-user@'+ip+' sudo yum install python3 -y'
       #SCPing the check_webserver.py file
       scp_check_webserver = "scp -o StrictHostKeyChecking=no -i assignment_key.pem check_webserver.py ec2-user@" + ip + ":."
       #change permissions to no
       ssh_change_permissions = "ssh -o StrictHostKeyChecking=no -i assignment_key.pem ec2-user@" + ip + " 'pwd'"
       #run checkwebserver
       run_file = 'ssh -t -o StrictHostKeyChecking=no -i assignment_key.pem ec2-user@' + ip + ' python3 check_webserver.py'

       #Running the ssh and scp commands and running the check_webserver:
       print ('Running: '+ssh_install_python)
       print ("")
       time.sleep(1)
       run(ssh_install_python, check=True, shell=True)
       print ('Running: '+scp_check_webserver)
       print ("")
       time.sleep(1)
       run(scp_check_webserver, check=True, shell=True)
       print ('Running: '+ssh_change_permissions)
       print ("")
       time.sleep(1)
       run(ssh_change_permissions, check=True, shell=True)
       print ('Running: '+run_file)
       print ("")
       time.sleep(1)
       run(run_file, check=True, shell=True)

    except CalledProcessError:
       print('Error 404!!')
       print('Try again!!')

#Calling all functions
def main():
    sec1 = security_group()
    ip = create_instance(sec1)
    check_web(ip)

if __name__ == '__main__':
    main()
   
    
 
