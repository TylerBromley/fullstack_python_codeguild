# practice_problem_1.py
import random

def is_even(a):
	return a % 2 == 0

print(is_even(5))
print(is_even(6))

def opposite(a, b):
	return (a > 0 and b < 0) or (a < 0 and b > 0)

print(opposite(10, -1))
print(opposite(2, 3))
print(opposite(-1, -1))

def near_100(num):
	return num in range(90, 111)

print(near_100(50))
print(near_100(99))
print(near_100(105))
print(near_100(100))
print(near_100(111))

def maximum_of_three(a, b, c):
	max3 = print(max(a, b, c))
	return max3


maximum_of_three(5, 6, 2)
maximum_of_three(-4, 3, 10)

def powers_of_2():
	for i in range(0, 21):
		return(2**i)

powers_of_2()


# Get a string from the user, print out another string, doubling every letter.
def double_letters(x):
	new_string = ""
	for i in x:
		new_string += (i*2)
	return new_string

print(double_letters('hello'))



# Write a function using random.randint to generate an index, use that index
# to pick a random element of a list and return it.
def random_element(fruit):
	return fruit[random.randint(0, len(fruit)-1)]

fruits = ['apples', 'bananas', 'pears']
print(random_element(fruits))


# Given a the two lists below, combine them into a dictionary.
def combine_dict(a, b):
	return dict(zip(a, b))

fruits = ['apples', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

print(combine_dict(fruits, prices))

# lists - problem three

def eveneven(nums):
	evens = [i for i in nums if i % 2 == 0]
	return len(evens) % 2 == 0
		
print(eveneven([5, 6, 2]))
print(eveneven([5, 5, 2]))

# comprehensions - problem 1
powers_of_2 = [2**i for i in range(10)]
print(powers_of_2)

def powers(n, r):
	return [n**i for i in range(r)]

print(powers(2, 20))
print(powers(4, 10))

# comprehensions - problem 3
first_dict = {1: 'a', 2: 'b'}
swapped = {k:v for (v, k) in first_dict.items()}

print(swapped)

# strings - problem 2
def missing_char(word):
	# char_list = []
	return [word[:i] + word[i+1:] for i in range(len(word))] 
	# for i in range(len(word)):
	# 	char_list.append(word[:i] + word[i+1:])
	# return char_list

print(missing_char("kitten"))





