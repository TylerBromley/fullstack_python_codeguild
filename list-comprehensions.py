# list-comprehensions.py

# list comprehensions are good for simple loops, with, say, 1 operation
# normal way
# one_to_ten = []
# for i in range(1, 11):
# 	one_to_ten.append(i)

# list comprehension
# [what you want to fill the list with, the loop to fill it]
one_to_ten = [i for i in range(1, 10)]

print(one_to_ten)

# map: mapping all elements of one list with the values of another
doubled = [x*2 for x in one_to_ten]
# equivalent to:
# doubled = []
# for x in one_to_ten:
# 	doubled.append(x*2)

print(doubled)

# FILTER
evens = [x for x in one_to_ten if (x % 2 == 0) and (x > 5)]
# equivalent to
# events = []
# for x in one_to_ten:
# 	if x % 2== 0;
# 	evens.append(x)

print(evens)

# COMBINING MAPS AND FILTERS
evens_plus_ten = [x+10 for x in one_to_ten if x % 2 == 0]

print(evens_plus_ten)

# MAPPING FUNCTIONS

def lookup_phone_number_by_name(name):
	""" Return the phone number of a person."""
	pass

names = ['David' 'Helen', 'Anne']
phone_numbers = [lookup_phone_number_by_name(name) for name in names]

# NESTED COMPREHENSIONS
# board = [[1,2,3], [4,5,6], [7,8,9]]

board = [[col for col in range(6)] for row in range(5)]

# equivalent to:

# rows = 5
# columns = 6
# board = []
# for row in range(rows):
# 	row = []
# 	for column in range(columns):
# 		row.append(column)
# 	board.append(row)

print(board)

# SET COMPREHENSIONS
{x // 10 for x in range(100)}

# DICT COMPREHENSIONS
fruits = {'a': 'apples', 'b': 'bananas', 'c': 'coconuts'}

fruits_cap = {k.upper():v.upper() for (k,v) in fruits.items()} 
# tuple unpacking is: for (k, v) in fruits.items()
print(fruits_cap)

fruits_without_a = {k:v for k,v in fruits.items() if v.find('a') == -1}

print(fruits_without_a)
























