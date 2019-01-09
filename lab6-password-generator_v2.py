# lab6-password-generator_v2.py

import random
import string

# get a list of lowercase and UPPERCASE letters
letters = string.ascii_lowercase + string.ascii_uppercase

# allow the user to set the length of the password
total_length = int(input("What size would you like your password? "))
password = []

# make a password list out of random characters, that is the size
# requested by the user
while len(password) <= total_length:
	password += random.choice(letters)

# print the resulting list joined as a string
print(''.join(password))