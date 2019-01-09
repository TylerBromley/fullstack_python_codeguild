# lab11-simple-calculator_v2.py

# create basic arithmetic functions
def add_nums(x, y):
	return x + y

def sub_nums(x, y):
	return x - y

def mult_nums(x, y):
	return x * y

def div_nums(x, y):
	return x // y

# Let the user continue performing operations until they say "done".
while True:
	# ask the user for type of operation
	user_input = input("What is the operation you'd like to perform? +, -, *, /" +
		               " or type 'done' to quit: ")
	# quit if user types "done"
	if user_input == "done":
		break
	# ask the user for x and y values
	x = int(input("What is the first number? "))
	y = int(input("What is the second number? "))
	
	# depending on which operation the user chose, call the appropriate
	# arithmetic function and print out the results
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
