# lab11-simple-calculator_v1.py

def add_nums(x, y):
	return x + y

def sub_nums(x, y):
	return x - y

def mult_nums(x, y):
	return x * y

def div_nums(x, y):
	return x // y

user_input = input("What is the operation you'd like to perform? +, -, *, / ")
x = int(input("What is the first number? "))
y = int(input("What is the second number? "))

if user_input == "+":
	result = add_nums(x, y)
	print(f"{x} + {y} = {result}")
elif user_input == "-":
	result = sub_nums(x, y)
	print(f"{x} - {y} = {result}")
elif user_input == "*":
	result = mult_nums(x, y)
	print(f"{x} * {y} = {result}")
elif user_input == "/":
	result = div_nums(x, y)
	print(f"{x} / {y} = {result}")