# lab4-magic8ball_v1.py

import random

# create a list of 8-ball responses
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

# have the user ask a question
user_question = input("Please ask the magic 8-ball a question: ")
# get a random answer from the prediction_list
answer = random.choice(prediction_list)
# print that answer
print(answer)