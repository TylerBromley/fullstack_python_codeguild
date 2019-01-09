# lab12-guess-the-number_v3.py

import random

# get a random number
number = random.randint(1, 10)

# let the user guess as many times as it takes, but each
# time, let them know if they are too high or too low
while True:
	user_num = int(input("Please guess a number between 1 and 10: "))

	if user_num == number:
		print("You win!")
		break
	elif user_num < number:
		print("Too low!")
	else:
		print("Too high!")
