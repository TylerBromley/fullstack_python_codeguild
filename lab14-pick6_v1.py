# lab14-pick6_v1.py

import random

def pick6():
	return [random.randint(1, 99) for i in range(6)] # six_list

def calculate_payout(winner, ticket):
	payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
	matches = 0

	for i in range(len(ticket)):
		if winner[i] == ticket[i]:
			matches += 1

	return payout[matches]


def main():

	winner = pick6()
	balance = 0
	for i in range(100000):
		ticket = pick6()
		balance -= 2
		winnings = calculate_payout(winner, ticket)
		balance += winnings
	print("balance: ", balance)


main()





