# lab7-rockpaperscissors_v1.py

import random

# a function that establishes what combinations win and lose
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

# start the player loop, ask the player for a selection
# randomly choose for the computer
while True:
	player_choice = input("Please choose rock, paper or scissors: ")
	computer_choice = random.choice(("rock", "paper", "scissors"))
	print(f"Computer choses {computer_choice}")

	# pass the two values to the calc_winner function as arguments
	calc_winner(player_choice, computer_choice)

	# ask the user if they'd like to play again
	play_again = input("Would you like to play again? [y/n]")
	# if not, break
	if play_again.lower().startswith('n'):
		break

	


	
