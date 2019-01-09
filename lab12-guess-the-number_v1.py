# lab12-guess-the-number_v1.py

import random

tries = 0
number = random.randint(1, 10)

while tries < 10:
	user_num = int(input("Please guess a number between 1 and 10: "))

	if user_num == number:
		print("You win!")
		break
	else:
		print("Try again!")
		tries += 1

