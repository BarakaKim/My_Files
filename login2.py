loop='true'
while (loop =='true'):
    name = input ('Enter your name: ')
    try:
        if (len (name) < 6):
            assert len (name) >6, 'Your Name has less than 6 characters'
    except AssertionError as msg:
        print (msg)
        input ('Re-enter name with six or more characters: ')
    else:
        print ('hello '+ name)
        loop='false'
