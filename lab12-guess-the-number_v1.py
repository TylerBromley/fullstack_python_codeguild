# lab12-guess-the-number_v1.py

import random

# create a count of triess and set it to 0
tries = 0
# get a random number between 1 and 10
number = random.randint(1, 10)

# give the use 10 tries to guess the number
while tries < 10:
	# get user guess
	user_num = int(input("Please guess a number between 1 and 10: "))

	# check if user guessed right
	if user_num == number:
		print("You win!")
		break
	# if not, and tries are not 10, let the user guess again
	else:
		print("Try again!")
		tries += 1

