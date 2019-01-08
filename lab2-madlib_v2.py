# lab2-madlib_v2.py

from random import shuffle
 
# Ask the user for groups of words
adjectives = input("Please enter 4 adjectives separated with spaces between: ")
nouns = input("Please enter 3 nouns separated by spaces: ")
ptvs = input("Please enter 2 past tense verbs: ")
adverbs = input("Please enter 2 adverbs: ")
verb = input("Please enter 1 verb: ")

# create lists by type and shuffle their order
adjectives = adjectives.split()
shuffle(adjectives)
nouns = nouns.split()
shuffle(nouns)
ptvs = ptvs.split()
shuffle(ptvs)
adverbs = adverbs.split()
shuffle(adverbs)

# print the madlib
print(f"Today I went to the zoo. I a saw a(n) {adjectives[0]} " +
	  f" {nouns[0]} jumping up and down in its tree.")
print(f"He {ptvs[0]} {adverbs[0]} through the large tunnel that led" + 
	  f" to its {adjectives[1]} {nouns[1]}.")
print(f"I got some peanuts and passed them through the cage to a" +
	  f" gigantic gray {nouns[2]} towering above my head. Feeding that" +
	  f" animal made me hungry.")
print(f"I went to get a {adjectives[2]} scoop of ice cream. It" +
	  f" filled my stomach. Afterwards I had to {verb} {adverbs[1]} to catch" +
	  f" our bus.") 
print(f"When I got home I {ptvs[1]} my mom for a {adjectives[3]}" +
	  f" day at the zoo.")
