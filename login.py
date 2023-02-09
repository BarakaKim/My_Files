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
