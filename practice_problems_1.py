# practice_problem_1.py

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