# lab18-peaks-and-valleys_v3.py

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def print_x(data):
	max_of_data = max(data)
	values = []
	line = ""
	has_one = False

	for i in range(10):
		for j in data:
			if j in values:
				line += " X "
				has_one = True
			elif has_one == True:
				line += " O "
			else:
				line += "   "
		has_one = False
		values.append(max_of_data)
		max_of_data -= 1
		print(line + "\n")
		line = ""

print_x(data)
