"""
[summary]
"""



# simple function that takes in two inputs and adds them together
def add_numbers(a, b):
	"""[summary]

	Arguments:
		a {[type]} -- [description]
		b {[type]} -- [description]
	"""
	print(a + b)


# Function for printing a hello statement
def hello():
	print('Hello')

def names(name, age):
	"""[summary]

	Arguments:
		name {[type]} -- [description]
		age {[type]} -- [description]
	"""
	print('こんにちは' + name + 'さん。君は' + age + '歳ですね')


add_numbers(3, 2)
hello()
names('れをる', '二十三')

def greet(name, version):
    """[summary]

	Arguments:
		name {[type]} -- [description]
		version {[type]} -- [description]
	"""
	print (f"This is {name} {str(version)}")
greet("UE", 4)

