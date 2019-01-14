# lab17-palindrome-and-anagram.py

from string import punctuation as punc

def palindrome(p_check):
	pal = p_check[::-1]
	if p_check == pal:
		return f"{p_check} is a palindrome"
	return f"{p_check} is not a palindrome"

def anagram(str1, str2):
    for i in punc:
        str1 = str1.replace(i, "")
        str2 = str2.replace(i, "")
    new_str1 = sorted(str1)
    new_str2 = sorted(str2)
    if new_str1 == new_str2:
        return f"{str2} is an anagram of {str1}!"
    return f"{str2} is not an anagram of {str1}!"

def main():
    print("Welcome to your palindrome and anagram checker!")
    p_check = input("Please enter a word to see if it's a palindrome: ").lower().replace(" ", "")
    print(palindrome(p_check))
    print("Anagram checker:")
    str1 = input("Please enter a word or phrase: ").lower().replace(" ", "")
    str2 = input("Please enter a potential anagram: ").lower().replace(" ", "")
    print(anagram(str1, str2))

main()