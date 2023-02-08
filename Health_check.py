#!/usr/bin/env python3
                #LOGIN SCRIPT
print ("AUTOMATIC COMPUTER HEALTH CHECK")
CorrectUsername = "BARAKA"
CorrectPassword = 123456

loop = 'true'
while (loop == 'true'):
    username = input("Please enter your username: ")
    if (username == CorrectUsername):
        password = int(input("Please enter your password: ")) # Input function always return a string, to convert a string to integer, we use int
        if (password == CorrectPassword):
            print ("Logged in successfully as " + username)
            loop = 'false'
        else:
            print ("Password incorrect!")
    else:
        print ("Username incorrect!")

                #SHUTIL AND PSUTIL MODULES
import shutil
import psutil
                    #SHUTIL
du = shutil.disk_usage ('/') # or shutil.disk_usage ('\\') using windows path
#print (psutil.disk_usage('/')) #disk usage using psutil
print (f'FREE DISK:{(du.free/du.total)*100} %') #the percentage of free disk
                     #PSUTIL
print (f'CPU PERCENTAGE: {psutil.cpu_percent(interval=1)}%')
print (f'CPU COUNT:{psutil.cpu_count ()}')
print ('\t')
print (F'VIRTUAL MEMORY:\n {psutil.virtual_memory()}')
print ('\t')
print (f'dISK PARTIONS:\n {psutil.disk_partitions()}')
print ('\t')
                    #INPUT FUNCTION, TRY AND EXCEPT FUNCTION
try:
    name = input ('For Computer Health Check, Please Enter your Computer Name:')
    assert name == 'BARAKA', 'You are not BARAKA, but proceed'
except AssertionError as msg: #this prevents our code to break whenever encours an error
    print (msg)
    print (f'WELCOME {name}, ')

print ('\t')
                #HEALTH CHECK IN A COMPUTER
print ('COMPUTER HEALTH STATUS')
#functions for cheking cpu and disk health
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75

#If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("Your Computer is UNHEALTH: Check your disk or CPU usage  ")
else:
    print('Your COMPUTER IS HEALTHY----Keep it up')
