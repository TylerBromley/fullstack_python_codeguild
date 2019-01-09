# lab12-guess-the-number_v5.py

import random

# get a number from user
user_num = int(input("Please enter a number between 1 and 10: "))


while True:
	# have the computer guess a random number
	computer_guess = random.randint(1, 10)
	# if computer guess is correct, end game
	if computer_guess == user_num:
		print("Computer wins!")
		break
	# if the computer guessed wrong, ask the user if they want the computer
	# to guess again
	else:
		print(f"Computer guessed {computer_guess}!")
		try_again = input("Would you like the computer to try again? [y/n] ")
		if try_again == "n":
			break
		