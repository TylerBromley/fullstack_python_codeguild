# lab13-ROT-Cipher_v1.py

from string import ascii_lowercase as alpha

sliced_list = list(alpha[13:] + alpha[:13])
encrypt_dict = dict(zip(alpha, sliced_list))
decrypt_dict = dict(zip(sliced_list, alpha))


def encrypt(user_input):
    encrypted_text = ""
    for i in user_input:
        encrypted_text += encrypt_dict.get(i, i)
    return encrypted_text


def decrypt(user_input):
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

    if options == "e":
        print(encrypt(user_input))
    elif options == "d":
        print(decrypt(user_input))

main()
