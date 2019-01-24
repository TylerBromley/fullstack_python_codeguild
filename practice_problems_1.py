# practice_problem_1.py
import random
import itertools
from functools import reduce
from collections import Counter


########FUNDAMENTALS##########
# fundamentals - problem 1
def is_even(a):
	return a % 2 == 0

print(is_even(5))
print(is_even(6))

# fundamentals - problem 2
def opposite(a, b):
	return (a > 0 and b < 0) or (a < 0 and b > 0)

print(opposite(10, -1))
print(opposite(2, 3))
print(opposite(-1, -1))

# fundamentals - problem 3
def near_100(num):
	return num in range(90, 111)

print(near_100(50))
print(near_100(99))
print(near_100(105))
print(near_100(100))
print(near_100(111))

# fundamentals - problem 4
def maximum_of_three(a, b, c):
	max3 = print(max(a, b, c))
	return max3

maximum_of_three(5, 6, 2)
maximum_of_three(-4, 3, 10)

# fundamentals - problem 5
def powers_of_2():
	for i in range(0, 21):
		return(2**i)

powers_of_2()

############STRINGS##############
# strings - problem 1
def double_letters(x):
	new_string = ""
	for i in x:
		new_string += (i*2)
	return new_string

print(double_letters('hello'))

# strings - problem 2
def missing_char(word):
	return [word[:i] + word[i+1:] for i in range(len(word))] 

print(missing_char("kitten"))

# strings - problem 3
def latest_letter(word):
	letters = sorted(word)
	return letters[-1]

print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis'))

# strings - problem 6
def count_letter(letter, word):
	count = 0
	for i in list(word):
		if i == letter:
			count += 1
	return count

print(count_letter('i', 'antidisestablishmentterianism'))
print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))

###########LISTS#############
# lists - problem 1
def random_element(fruit):
	return fruit[random.randint(0, len(fruit)-1)]

fruits = ['apples', 'bananas', 'pears']
print(random_element(fruits))

# lists - problem three
def eveneven(nums):
	evens = [i for i in nums if i % 2 == 0]
	return len(evens) % 2 == 0
		
print(eveneven([5, 6, 2]))
print(eveneven([5, 5, 2]))

# lists - problem 7
nums1 = [1, 5, 9, 7, 3]
nums2 = [2, 5, 3, 8, 4]

def common_elements(nums1, nums2):
	# return [i for i in nums1 if i in nums2]
	return list(set(nums1) & set(nums2)) # '&' finds the intersection

print(common_elements(nums1, nums2))

# lists - problem 8
def combine(nums1, nums2):
	#return [i for i in itertools.chain.from_iterable(zip(nums1, nums2))]
	return [i for j in zip(nums1, nums2) for i in j] #[:-1]

print(combine(['a','b','c'],[1,2,3]))

# lists - problem 11
nums = [[5,2,3],[4,5,1],[7,6,3]]
def combine_all(nums):
	return [j for i in range(len(nums)) for j in nums[i]]

	# using reduce:
	# return reduce(lambda x, y: x+y, nums)

print(combine_all(nums))

# Lists - problem 13
def minimum(nums):
	nums.sort(reverse=True)
	return nums.pop()

	running_min = float('inf')
	for num in nums:
		if num < running_min:
			running_min = num
	return running_min

def maximum(nums):
	nums.sort()
	return nums.pop()

	running_max = float('-inf')
	for num in nums:
		if num > running_max:
			running_max = num
	return running_max

def mean(nums):
	total = 0
	for i in nums:
		total += i
	return total / len(nums)

def mode(nums):
	count = {}
	for num in nums:
		if num not in count:
			count[num] = 1
		else:
			count[num] += 1
	return max(count.items(), key=lambda x:x[1])[0]

print(minimum([9, 8, 3, 7, 2, 6, 5, 4]))
print(maximum([9, 8, 3, 7, 2, 6, 5, 4]))
print(mean([9, 8, 3, 7, 2, 6, 5, 4]))
print(mode([2,2,4,3]))

########DICTIONARIES###########
# dictionaries - problem 1
def combine_dict(a, b):
	return dict(zip(a, b))

fruits = ['apples', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

print(combine_dict(fruits, prices))

#########COMPREHENSIONS###########
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


# factorials n!
# 3! = 6
# 4! = 24
# 5! = 120
# n(n -1)!

# recursion
def fac(n):
	if n == 0:
		return 1
	return n * fac(n-1)

def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

cached_fibonacci = [0,1]
def memoized_fibonacci(n):
	if n < len(cached_fibonacci):
		return cached_fibonacci[n]
	if n == 0:
		return 0
	if n == 1:
		return 1
	fib = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
	cached_fibonacci.append(fib)
	return fib

def binary_search(l, target, start, end):
	if start >= end:
		return 'Not found'

	mid = start + (end - start)/2
	if l[mid] == target:
		return mid

	if l[mid] < target:
		return binary_search(l, target, mid+1, end)

	if l[mid] > target:
		return binary_search(l, target, start, mid)

# lists problem 12
def fib(n):
	return [calc_fib(i) for i in range(n)]

def calc_fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return calc_fib(n-2) + calc_fib(n-1)

print(fib(10))




	













