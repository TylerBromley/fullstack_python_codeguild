# lab12-guess-the-number_v4.py

import random

number = random.randint(1, 10)
print(number)

last_guess = 0

while True:
	user_num = int(input("Please guess a number between 1 and 10: "))
	print(last_guess)
	if user_num == number:
		print("You win!")
		break
	elif user_num < number:
		print("Too low!")
		if abs(user_num - number) == abs(last_guess - number):
			print("Keep going!")
		elif abs(user_num - number) < abs(last_guess - number):
			print("You are getting warmer.")
		elif abs(user_num - number) > abs(last_guess - number):
			print("You're getting colder.")
		
		last_guess = user_num

	else:
		print("Too high!")
		if abs(user_num - number) == abs(last_guess - number):
			print("Keep going!")
		elif (user_num - number) < (last_guess - number):
			print("You are getting warmer.")
		elif (user_num - number) > (last_guess - number) :
			print("You're getting colder.")
\
		last_guess = user_num