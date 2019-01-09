# lab12-guess-the-number_v2.py

import random

number = random.randint(1, 10)

while True:
	user_num = int(input("Please guess a number between 1 and 10: "))

	if user_num == number:
		print("You win!")
		break
	else:
		print("Try again!")