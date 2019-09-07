"""
Should be used only when dealing with large numbers & data sets
"""

from array import array

# Arrays can use most of the same methods as lists
# When running a method for adding/removing an item, the data type be of the same as in the orginal variable
numbers = array('i', [1,2,3])
numbers.append(4)
print (numbers)
