try:
    name = input ('Enter your Name: ')
    assert len (name) > 6, "your name has less than 6 characters"
    print ('Hello ' +  name + ',you are welcome')
except AssertionError as msg: #this prevents our code to break whenever encours an error
    print (msg)
    input ('Re-Enter your Name with 6 or more characters: ')

print ('\t')

def test_sum():
    """ Testing the function of adding number"""
    assert sum([1, 2, 3]) == 6, "INCORRECT: The answer is 6" # syntax--- assert <expression>, <message if there is an error>
    print ('TEST1: there is no error in summation function')

assert pow(2,3) == 8, "INCORRECT: The answer is 8" # syntax--- assert <expression>, <message if there is an error>
print ('TEST2: there is no error in a function for exponents')

assert (2*2) == 4, "INCORRECT: The answer should be 4"
print ('TEST3: there is no error in Square function')
print ('\t')
if __name__ == "__main__":
    test_sum()
    print("Everything passed")
