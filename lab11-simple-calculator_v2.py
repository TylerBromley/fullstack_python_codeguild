# lab11-simple-calculator_v2.py

# return basic arithmetic functions
def eval_nums(user_input, x, y):
	if user_input == "+":
		return x + y
	elif user_input == "-":
		return x - y
	elif user_input == "*":
		return x * y
	else:
		return x // y

def main():
# Let the user continue performing operations until they say "done".
	while True:

		while True:
			# ask the user for type of operation
			try:
				user_input = input("What is the operation you'd like to perform? '+', '-', '*' or '/': ")
				# quit if user types "done"
				if user_input not in ('+', '-', '*', '/'):
					raise ValueError
				else:
					break
			except ValueError:
				print("Please enter a valid symbol")

		# ask the user for x and y values
		while True:
			try:
				x = int(input("What is the first number? "))
				break
			except ValueError:
				print("Please enter a valid number!")

		while True:
			try:
				y = int(input("What is the second number? "))
				break
			except ValueError:
				print("Please enter a valid number!")
		
		#print the expression and results
		print(f"{x} {user_input} {y} = {eval_nums(user_input, x, y)}")
		play_again = input("Press enter to play again or 'done' to exit: ").strip().lower()
		if play_again == "done":
				break
main()
