# lab15-number-to-phrase.py

# convert a given number to its english representation.

tens_dict = {0: "", 1: "teen", 2: "twenty", 3: "thirty", 4: "forty",
			 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
ones_dict = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
			 6: "six", 7: "seven", 8: "eight", 9: "nine"}

def phrase_gen(n):
	for i in range(n):
		hundreds_digit = i//100
		tens_digit = (i % 100) // 10
		ones_digit = i%10
		if hundreds_digit == 0:
			if tens_digit == 0 and ones_digit == 0:
				print("zero")
			elif tens_digit == 0 and ones_digit > 0:
				print(ones_dict[ones_digit])
			elif tens_digit == 1 and ones_digit == 0:
				print("ten")
			elif tens_digit == 1:
				if ones_digit == 1:
					print("eleven")
				elif ones_digit == 2:
					print("twelve")
				elif ones_digit == 3:
					print("thirteen")
				elif ones_digit == 5:
					print("fifteen")
				else:
					print(ones_dict[ones_digit] + tens_dict[tens_digit])
			elif ones_digit == 0:
				print(tens_dict[tens_digit])
			else:
				print(tens_dict[tens_digit] + "-" + ones_dict[ones_digit])

		elif hundreds_digit > 0:
			if ones_digit == 0 and tens_digit == 0:
				print(ones_dict[hundreds_digit] + " hundred")
				#print(f"{hundreds_dict[hundreds_digit]} hundred and {tens_dict[tens_digit]}")
			elif tens_digit == 0:
				print(ones_dict[hundreds_digit] + " hundred " + ones_dict[ones_digit]) 
			elif tens_digit == 1 and ones_digit == 0:
				print(ones_dict[hundreds_digit] + " hundred ten" )
			elif ones_digit == 0:
				print(ones_dict[hundreds_digit] + " hundred " + tens_dict[tens_digit])
			elif tens_digit == 1:
				if ones_digit == 1:
					print(ones_dict[hundreds_digit] + " hundred eleven")
				elif ones_digit == 2:
					print(ones_dict[hundreds_digit] + " hundred twelve")
				elif ones_digit == 3:
					print(ones_dict[hundreds_digit] + " hundred thirteen")
				elif ones_digit == 5:
					print(ones_dict[hundreds_digit] + " hundred fifteen")
				else:
					print(ones_dict[hundreds_digit] + " hundred " + ones_dict[ones_digit] + tens_dict[tens_digit])
			else:
				print(ones_dict[hundreds_digit] + " hundred and " + tens_dict[tens_digit] + "-" + ones_dict[ones_digit])


phrase_gen(1000)



