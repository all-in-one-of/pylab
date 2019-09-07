"""
[summary]
"""
items = [
    ('Products 3', 10),
    ('Products 7', 9),
    ('Products 1', 12)
]

# Using the map funciton to map an item to a new list
prices = list(map(lambda item:item[1], items))

# Filter out items from an iterable into a new list based on a condition
filtered = list(filter(lambda item: item[1] >= 10, items))

# Using list comprehension to get an item from a list USE THIS!!!
# [expression for item in items]
prices = [x[1] for x in items]
print (prices)

# Using list comprehension to filter an item based on a boolean condition
filtered = [i for i in items if i[1]<10]
print (filtered)
