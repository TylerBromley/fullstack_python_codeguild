# lab19-blackjack-advice_v1.py

def advise(cards_list, cards_dict):
	total = 0
	response = ""
	for i in cards_list:
		if i in cards_dict:
			total += cards_dict.get(i)
	if total < 17:
		response += f"{total} Hit"
	elif total < 21:
		response += f"{total} Stay"
	elif total == 21:
		response += f"{total} Blackjack!"
	else:
		response += f"{total} Busted!"
	return response

def main():
	try:
		player_cards1 = input("What's your first card? ").strip().upper()
		player_cards2 = input("What's your second card? ").strip().upper()
		player_cards3 = input("What's your third card? ").strip().upper()
	except ValueError:
		print("That's not a valid card.")

	cards_list = list(player_cards1 + player_cards2 + player_cards3)

	cards_dict = {"A": 1, "2": 1, "3": 3, "4": 4, "5": 5,
				  "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
				  "J": 10, "Q": 10, "K": 10}

	print(advise(cards_list, cards_dict))

main()
