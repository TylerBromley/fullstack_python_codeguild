# lab6_password_generator_v3.py

import string
import random

while True:
	# ask the user for length of password, by character type
	lower_num = int(input("Please enter how many lowercase letters: "))
	upper_num = int(input("please enter how many uppercase letters: "))
	num_num = int(input("Please enter how many digits: "))
	punc_num = int(input("Please enter how many special characters: "))

	# get each character type
	alpha_low = string.ascii_lowercase
	alpha_up = string.ascii_uppercase
	digits = string.digits
	punc = string.punctuation
	password = []

	# add random values from each character list
	for i in range(0, lower_num):
	    password += random.choice(alpha_low)

	for i in range(0, upper_num):
	    password += random.choice(alpha_up)

	for i in range(0, num_num):
	    password += random.choice(digits)

	for i in range(0, punc_num):
	    password += random.choice(punc)

	# shuffle the list
	random.shuffle(password)
	# convert list back to a string
	print(''.join(password))
	satisfied = input("Are you satisfied with your password? [y/n] ")
	if satisfied.lower().startswith("y"):
		break