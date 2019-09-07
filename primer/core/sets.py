"""
A collection of items with no duplicates denoted by the {}
"""
numbers = [1,1,2,3,4]
first = set(numbers)
second = {1,5}

# A standard set command that gets only the unique items from a list 
print (first)

# Adding an item to a set
second.add(6)
print (second)

# Removing an item to a set
second.add(6)
second.remove(6)
print (second)

# Getting the length of a set
print (len(second))

# Joins the values of two sets into a new set
print (first | second)

# Returns the values that exists in both sets
print (first & second)

# Returns the difference between two sets
print (first - second)

# Return the values are exists in either sets but not both
print (first ^ second)

# Sets do not support indexing therefor run it through a loop if you need to look for an item
if 3 in first:
    print ('yes')

# Using List comprehension to count the number of occurences an item appears in a set
x = 3
yes = [x for x in first]
print (yes.count(x))

# A simple set comprehension returns a range of 5 values & multiplies them by 2 
values = {x * 2 for x in range(5)}
print (values)