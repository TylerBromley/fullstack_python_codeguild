# lab12-guess-the-number_v5.py

import random


user_num = int(input("Please enter a number between 1 and 10: "))

while True:
	
	computer_guess = random.randint(1, 10)
	if computer_guess == user_num:
		print("Computer wins!")
		break
	else:
		print(f"Computer guessed {computer_guess}!")
		try_again = input("Would you like the computer to try again? [y/n] ")
		if try_again == "n":
			break
		