
"""
Dictionaries are similar to lists except that they use keys to point to specific values.
Dictionaries can also be stored/read from other more mutable formats like JSON.
Dictionary keys need to be unique.
Dictionaries are non indexable
"""

monthConversions = {
    'Jan': '一ヶ月',
    'Feb': '二ヶ月',
    'Mar': '三ヶ月',
    'Apr': '四ヶ月',
    'May': '五ヶ月',
    'Jun': '六ヶ月',
    'Jul': '七ヶ月',
    'Aug': '八ヶ月',
    'Sep': '九ヶ月',
    'Oct': '十ヶ月',
    'Nov': '十一ヶ月',
    'Dec': '十二ヶ月'
}

# Printing a specific dictionary key value
print(monthConversions['Mar'])

# A standard dictionary consisting of two keys 
point = {'x': 1, 'y': 2}

# Using the dict() function to create a dictionary
point = dict(x=1, y=2)
print(point['x'])

# Adding a new dictionary item
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
print (point)

# Using a loop to check if a key exists inside a dictionary
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
if 'a' in point:
    print (point['a'])

# Using the get method to check if a key exists inside a dictionary. 
# Results key value if successful
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
完成 = point.get('z')
print (完成)

# Sets a default value if a key does not exist
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
完成 = point.get('a', 0)
print (完成)

# Deletes a dictionary item
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
del point['x']
print (point)

# Using a for loop to iterate over a dictionary
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
for key in point:
    print(key, point[key])

# Using the items() in a for loop to return a tuple of the dictionary item
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
for item in point.items():
    print(item)

# Unpacking a key & key value item from a dictionary
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
for key, value in point.items():
    print(key, value)

# A simple dict comprehension that creates a dictionary with 5 keys & multiplies each value by 2
values = {x: x * 2 for x in range(5)}
print (values)