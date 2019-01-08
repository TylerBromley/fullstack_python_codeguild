# lab6_password_generator.py

import random
import string

# letters == ""
letters = string.ascii_lowercase + string.ascii_uppercase

password = []
total_length = random.randint(5, 20)

while len(password) <= total_length:
	password += random.choice(letters)

# convert to a string
print(''.join(password))
