# lab6-password-generator_v2.py

import random
import string

letters = string.hexdigits

total_length = int(input("What size would you like your password? "))
password = []

while len(password) <= total_length:
	password += random.choice(letters)

print(''.join(password))