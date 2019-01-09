# lab10-average-numbers_v2.py

nums = []
total = 0
count = 0


while True:
	user_input = input("Please enter a number or 'done' ")

	if user_input.strip().lower() == "done":
		break
	else:
		nums.append(int(user_input))

for num in nums:
	total += num

for i in range(len(nums)):
	count += 1

print(total)
print(count)
average = total / count

print(average)