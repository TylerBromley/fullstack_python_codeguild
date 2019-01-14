# lab20-credit-card-validator.py

nums = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5".split()
check_digit = int(nums.pop())
nums.reverse()

def validate(nums):
	nums = [int(i[1])*2 if (i[0]%2==0) else int(i[1]) for i in enumerate(nums)]
	nums = sum([i - 9 if i > 9 else i for i in nums])%10
	if nums == check_digit:
		return "Valid!"
	return "Invalid"

print(validate(nums))