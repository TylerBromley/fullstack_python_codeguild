# lab14-pick6_v2.py

import random


def pick6():
	six_list = []
	for i in range(6):
		six_list.append(random.randint(0, 100))
	return six_list

def match_numbers(pick6):
	winner = pick6()
	print(f"Winning ticket is {winner}")
	expenses = 0
	earnings = 0
	for i in range(100000): #100000
		purchased_ticket = pick6()
		expenses += 2.00
		count = 0
		for i in range(6):
			if purchased_ticket[i] == winner[i]:
				count += 1
		if count == 6:
			earnings += 25000000
			print(f"******6 matches: {purchased_ticket}")
		elif count == 5:
			earnings += 1000000
			print(f"*****5 matches: {purchased_ticket}")
		elif count == 4:
			earnings += 50000
			print(f"****4 matches: {purchased_ticket}")
		elif count == 3:
			earnings += 100
			print(f"***3 matches: {purchased_ticket}")
		elif count == 2:
			earnings += 7
		elif count == 1:
			earnings += 4

	roi = (earnings - expenses) / expenses
	return  earnings, expenses, roi

print(match_numbers(pick6))