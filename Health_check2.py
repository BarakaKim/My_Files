#CREATE ACCOUNT AND LOGIN
print ("CREATE YOUR ACCOUNT")

import maskpass

loop='true'
while (loop =='true'):
try:
name = input ('Enter your Name: ')
#pasw = input ('Enter your Password: ')
pasw = maskpass.advpass()
assert len(pasw) > 6, 'Your Password has to be more than 6 characters'
except AssertionError as msg:
print (msg)

if (len (pasw) <= 6):
loop = 'true'
else:
print ('hello '+ name + ', You have successful created your account')
loop = 'false'

CorrectUsername = name
CorrectPassword = pasw
print ('\t')
print ("LOGIN WITH YOUR CREATED ACCOUNT")
loop = 'true'
while (loop == 'true'):
username = input("Please enter your username: ")
if (username == CorrectUsername):
password = maskpass.advpass() # Input function always return a string, to convert a string to integer, we use int
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
print ('\t')
#INPUT FUNCTION, TRY AND EXCEPT FUNCTION
print ('WELCOME TO CHECK YOUR COMPUTER HEALTH')
try:
name = input ('Please Enter your Computer Name:')
assert name == 'BARAKA', 'You are not BARAKA, JUST WAIT'
except AssertionError as msg: #this prevents our code to break whenever encours an error
print (msg)
print (f'WELCOME {name}, ')

print ('\t')
#HEALTH CHECK IN A COMPUTER
print ('YOUR COMPUTER STATUS')
#functions for cheking cpu and disk health
def check_disk_usage(disk):
"""Verifies that there's enough free space on disk"""
du = shutil.disk_usage(disk)
free = du.free / du.total * 100
return free > 20

def check_cpu_usage():
"""Verifies that there's enough unused CPU"""
usage = psutil.cpu_percent(1)
print (f'your CPU percentage use is: {usage}')
return usage < 75

print ("---------------------------------------------------------------")
print (f'FREE DISK SPACE: {(shutil.disk_usage("/").free/shutil.disk_usage("/").total *100)}') #we have use double qoutes to avoid f-string unmatched error
print (f'CPU PERCENTAGE: {psutil.cpu_percent(interval=1)}%')
print ("===============================================================")
#If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
print(name + ", Your  COMPUTER is UNHEALTH: Fix your DISK or CPU usage")
else:
print(name + ', Your COMPUTER IS HEALTHY----Keep it up')
