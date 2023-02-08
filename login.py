print ("")

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
