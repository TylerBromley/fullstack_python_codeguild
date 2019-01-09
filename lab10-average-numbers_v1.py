# lab10-average-numbers_v1.py

nums = [1, 2, 3, 4, 5, 6, 7]
total = 0
count = 0

for num in nums:
	total += num

for i in range(len(nums)):
	count += 1

average = total / count

print(average)


