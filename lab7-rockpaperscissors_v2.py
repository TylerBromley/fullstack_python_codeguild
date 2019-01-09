# lab7-rockpaperscissors_v1.py

import random

def calc_winner(player_choice, computer_choice):
	defeats = {'rock': 'scissors',
			   'paper': 'rock',
			   'scissors': 'paper'}

	if player_choice == computer_choice:
		print("It's a tie!")
	elif defeats[player_choice] == computer_choice:
		print("Player wins!")
	else:
		print("Computer wins!")

while True:
	player_choice = input("Please choose rock, paper or scissors: ")
	computer_choice = random.choice(("rock", "paper", "scissors"))
	print(f"Computer choses {computer_choice}")

	calc_winner(player_choice, computer_choice)

	play_again = input("Would you like to play again? [y/n]")
	if play_again.lower().startswith('n'):
		break

	# def calc_winner(computer_choice, player_choice):
	# if player_choice == computer_choice:
	# 	print("It's a tie!")
	# elif player_choice == "rock": 
	# 	if computer_choice == "paper":
	# 		print("Computer chose paper. You lose!")
	# 	else:
	# 		print("Computer chose scissors. You win!")
	# elif player_choice == "paper":
	# 	if computer_choice == "scissors":
	# 		print("Computer chose scissors. You lose!")
	# 	else:
	# 		print("Computer chose rock. You win!")
	# else:
	# 	if computer_choice == "rock":
	# 		print("Computer chose rock. You lose!")
	# 	else:
	# 		print("Computer chose paper. You win!")

	


	
