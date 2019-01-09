# lab10-average-numbers_v2.py

# create an empty list for the user numbers
nums = []
# set a total and a count
total = 0
count = 0

# ask the user for as many numbers as they want to average
# keep adding numbers to the nums list until the user types "done"
while True:
	user_input = input("Please enter a number or 'done' ")

	if user_input.strip().lower() == "done":
		break
	else:
		nums.append(int(user_input))

# get the total by adding the numbers together
for num in nums:
	total += num

# crerate an average by dividing the total by the count
for i in range(len(nums)):
	count += 1

# get the average by dividing the total by the count
average = total / count
# print out the average
print(average)