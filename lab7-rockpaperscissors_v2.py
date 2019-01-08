# lab7-rockpaperscissors_v1.py

import random

while True:
	player_choice = input("Please choose rock, paper or scissors: ")
	computer_choice = random.choice(("rock", "paper", "scissors"))

	if player_choice == computer_choice:
		print("It's a tie!")
	elif player_choice == "rock": 
		if computer_choice == "paper":
			print("Computer chose paper. You lose!")
		else:
			print("Computer chose scissors. You win!")
	elif player_choice == "paper":
		if computer_choice == "scissors":
			print("Computer chose scissors. You lose!")
		else:
			print("Computer chose rock. You win!")
	else:
		if computer_choice == "rock":
			print("Computer chose rock. You lose!")
		else:
			print("Computer chose paper. You win!")

	play_again = input("Would you like to play again? [y/n]")

	if play_again.lower().startswith('n'):
		break