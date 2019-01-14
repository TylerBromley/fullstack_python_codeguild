# lab15-number-to-phrase_v2.py

tens_dict = {0: "", 1: "teen", 2: "twenty", 3: "thirty", 4: "forty",
			 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
ones_dict = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
			 6: "six", 7: "seven", 8: "eight", 9: "nine"}


for i in range(100):
	tens_digit = i // 10
	ones_digit = i%10
	written = ""

	if tens_digit == 0:
		if ones_digit == 0:
			written = "zero"
		else:
			written = ones_dict[ones_digit]
	else:
		if tens_digit == 1:
			if ones_digit == 0:
				written = "ten"
			elif ones_digit == 1:
				written = "eleven"
			elif ones_digit == 2:
				written = "twelve"
			elif ones_digit == 3:
				written = "thirteen"
			elif ones_digit == 5:
				written = "fifteen"
			else:
				written = ones_dict[ones_digit] + tens_dict[tens_digit]
		elif tens_digit > 1:
			if ones_digit == 0:
				written = tens_dict[tens_digit]
			else:
				written = tens_dict[tens_digit] + "-" + ones_dict[ones_digit]

	print(written)