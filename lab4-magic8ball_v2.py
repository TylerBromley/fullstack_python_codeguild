# lab4-magic8ball.py

import random

prediction_list = [
	"It is certain",
	"It is decidedly so",
	"Without a doubt",
	"Yes definitely",
	"You may rely on it",
	"As I see it, yes",
	"Most likely",
	"Outlook good",
	"Yes",
	"Signs point to yes", 
	"Reply hazy, try again", 
	"Ask again later", 
	"Better not tell you now",
	"Cannot predict now",
	"Concentrate and ask again",
	"Don't count on it",
	"My reply is no",
	"My sources say no",
	"Outlook not so good",
	"Very doubtful",
]

print("\nWelcome, user!")

while True:

	user_question = input("Please ask the magic 8-ball a question: ")
	answer = random.choice(prediction_list)
	print('\n' + answer)
	again_question = input("\nWould you like to play again? ")

	if again_question.lower().startswith('n'):
		print("\nGoodbye!")
		break

	

	
