# lab11-simple-calculator_v1.py

# create basic arithmetic functions
def add_nums(x, y):
	return x + y

def sub_nums(x, y):
	return x - y

def mult_nums(x, y):
	return x * y

def div_nums(x, y):
	return x // y

# ask user what kind of operation they'd like to perform
user_input = input("What is the operation you'd like to perform? +, -, *, / ")
# ask the user for two values
x = int(input("What is the first number? "))
y = int(input("What is the second number? "))

# call the user-selected function and print the result
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