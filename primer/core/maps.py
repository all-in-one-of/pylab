"""
[summary]
"""
items = [
    ('Products 1', 10),
    ('Products 2', 9),
    ('Products 3', 12)
]

# Using the map function in conjunction with a lambda expression to map a tuple item from a list to a variable
x = map(lambda item:item[1], items)
for item in x:
    print (item)

# Using the map function in conjunction with a lambda expression to map a tuple item from a list to a variable
# The map function takes a lambda expression and applies it on every item of an iterable
prices = list(map(lambda item:item[1], items))
print (prices)

# The filter function uses a boolean condition to determine which items in an iterable to return
filtered = list(filter(lambda item: item[1] >= 10, items))
print (filtered)


