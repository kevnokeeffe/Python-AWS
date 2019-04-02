#!/usr/bin/python3

# Python Text Interface
# Ref1: https://docs.python.org/2/library/subprocess.html
# Ref2: https://github.com/Coady1991/aws-automate-scripts
import os
import subprocess
import time

# Menu deisgn
def print_menu():
    print ('')
    print ("     ","------------Menu------------")
    print ("     ","|                          |")
    print ("     ","|-----Instance Options-----|")
    print ("     ","|                          |")
    print ("     ","|1. Create a New Instance  |")
    print ("     ","|2. List Instances         |")
    print ("     ","|3. Terminate Instance     |")
    print ("     ","|                          |")
    print ("     ","|------Bucket options------|")
    print ("     ","|                          |")
    print ("     ","|4. Create a New Bucket    |")
    print ("     ","|5. List Buckets           |")
    print ("     ","|6. Delete Bucket          |")
    print ("     ","|7. Put Bucket             |")
    print ("     ","|                          |")
    print ("     ","|8. Add File to Instance   |")
    print ("     ","|0. Exit                   |")
    print ("     ","----------------------------")

looping = True

# While loop continues until loop = False
while looping:
    # Displays the menu above
    print_menu()
    choice = input("       Please select an option: ")

    if choice == "1":
        subprocess.call(['python3', 'run_new_webserver.py'])
        print (2 * '\n')
    elif choice == "2":
        subprocess.call(['python3', 'list_instances.py'])
        print('')
        #Prompts user to return to menu
        input('Press any key to return to menu')
        print (2 * '\n')
    elif choice == "3":
        subprocess.call(['python3', 'terminate_instances.py'])
        print (2 * '\n')
    elif choice == "4":
        subprocess.call(['python3', 'create_bucket.py'])
        print('')
        input('Press any key to return to menu')
        print (2 * '\n')
    elif choice == "5":
        subprocess.call(['python3', 'list_buckets.py'])
        print('')
        input('Press any key to return to menu')
        print (2 * '\n')
    elif choice == "6":
        subprocess.call(['python3', 'delete_buckets.py'])
        print (2 * '\n')
    elif choice == "7":
        subprocess.call(['python3', 'put_bucket.py'])
        print (2 * '\n')
    elif choice == "8":
        subprocess.call(['python3', 'add_file_update.py'])
        print (2 * '\n')
    elif choice == "0":
        # loop set to False, exits menu
        time.sleep(.5)
        print("Good Buy")
        time.sleep(.5)
        looping = False
        exit()
    else:
        # Clears the screen and prints an error message for invalid input
        os.system('clear')
        print('Please enter a valid option')

