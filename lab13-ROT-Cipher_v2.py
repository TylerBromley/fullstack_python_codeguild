# lab13-ROT-Cipher_v2.py

from string import ascii_lowercase as alpha

def encrypt(user_input, encrypt_dict):
	encrypted_text = ""
	for i in user_input:
		encrypted_text += encrypt_dict.get(i, i)
	return encrypted_text

def decrypt(user_input, decrypt_dict):
	decrypted_text = ""
	for i in user_input:
		decrypted_text += decrypt_dict.get(i, i)
	return decrypted_text

def main():
	# ask user for the word or phrase, validate that there are no numbers
	while True:
		try:
			user_input = list(input("Please enter a message: ").lower())
			if any(s.isdigit() for s in user_input):
				raise ValueError()
			break
		except ValueError:
			print("Letters only please!")
	# ask user for the method: encrypt or decrypt, 
	# validate the input is 'e' or 'd'
	while True:
		try:
			options = input("Please enter 'e' for 'encrypt' " + 
				                    "or 'd' for decrypt: ").strip().lower()
			if (options != 'e') and (options != 'd'):
				raise ValueError()
			break
		except ValueError:
			print("Please enter 'e' or 'd'")
	# ask user for rotation rate
	while True:
		try:
			rotate = int(input("Please enter by how many places " +
				               "you'd like to rotate: "))
			break
		except ValueError:
			print("Numbers only please!")

	# declare variables
	sliced_list = list(alpha[rotate % 26:] + alpha[:rotate % 26])
	encrypt_dict = dict(zip(alpha, sliced_list))
	decrypt_dict = dict(zip(sliced_list, alpha))

	if options == "e":
		print(encrypt(user_input, encrypt_dict))
	elif options == "d":
		print(decrypt(user_input, decrypt_dict))

main()