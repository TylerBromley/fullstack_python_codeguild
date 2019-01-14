# lab18-peaks-and-valleys_v2.py
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def print_x(data):
	max_of_data = max(data)
	values = []
	line = ""
	for i in range(0, len(set(data))+1):
		for j in data:
			if j in values:
				line += "X  "
			else:
				line += "   "
		values.append(max_of_data)
		max_of_data -= 1
		print(line + "\n")
		line = ""

print_x(data)
