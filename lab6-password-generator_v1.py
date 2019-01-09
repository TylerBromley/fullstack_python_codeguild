# lab6_password_generator.py

import random
import string

# get a list of lowercase and UPPERCASE letters
letters = string.ascii_lowercase + string.ascii_uppercase

# assign an empty list to the password variable
password = []
# get a random password length and store it in total_length
total_length = random.randint(5, 20)

# as long as the total random length has not been reached, append
# random letters from the letters variable
while len(password) <= total_length:
	password += random.choice(letters)

# convert to a string
print(''.join(password))
