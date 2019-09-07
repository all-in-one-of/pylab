"""
[summary]
"""

# Data structure that can store multiple forms of data
# Tuples are immutable which means they can't be changed or modified
# Tuples should be used on data that you don't want changed/modified
# A single tuple
coordinates = (4,5)

# A list of tuples
listCoordinates = [(4,5), (6,7), (80,34)]
# print(coordinates[0])

# Converts a list into a tuple
point = tuple([1,2])
print(point)

# Converts a string into a tuple
char = tuple('鈴木里奈')
print (char)

# Swapping variables
x = 10
y = 11
x, y = y, x
print ('x', x)
print ('y', y)

# Using the zip function to combine two lists into a tuple
list1 = [1,2,3]
list2 = [10,20,30]
combined = list(zip('abc', list1, list2))
x = [i for i in combined[0:2]]
print (combined)
print (x)
