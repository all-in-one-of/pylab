"""
[summary]
"""

#   vars
myInt = 100
string = "foo"
myFloat = 1.25
myBool = True

# printing strings in python 3
print("Python 3")

# printing strings in python 2
print ("Python 2.7")


# block comments for docstrings
'''
This is a block comment
'''

# printing variable types
print(type(myInt))
print(type(string))
print(type(myFloat))
print(type(myBool))

# printing a type conversion
print(type(float(myInt)))
print(type(str(myFloat)))
print(type(int(myBool)))

# combining data types
def add_numbers(a: int, b: int):
    """[summary]
    
    Arguments:
        a {int} -- [description]
        b {int} -- [description]
    """
    print(a + b)


# Swapping variables
x = 10
y = 11

x, y = y, x

print ('x', x)
print ('y', y)