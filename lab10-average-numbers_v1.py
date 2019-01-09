# lab10-average-numbers_v1.py

# create a list of numbers
nums = [1, 2, 3, 4, 5, 6, 7]
# set a total and a count
total = 0
count = 0

# get the total by adding the numbers together
for num in nums:
	total += num

# get a count of all the numbers in nums
for i in range(len(nums)):
	count += 1

# crerate an average by dividing the total by the count
average = total / count

# print out the average
print(average)


