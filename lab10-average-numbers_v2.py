# lab10-average-numbers_v2.py

def get_average():
	nums = []

	while True:
		user_input = input("Please enter a number or 'done' ")
		if user_input.strip().lower() == "done":
			break
		else:
			nums.append(int(user_input))
	print(sum(nums)/len(nums))

get_average()