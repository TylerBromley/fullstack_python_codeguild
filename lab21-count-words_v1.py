# lab21-count-words.py

import string

translator = str.maketrans("", "", string.punctuation)
with open('heart-of-darkness.txt') as f:
	word_list = f.read().lower().translate(translator).split()

def get_word_count(word_list):
	word_count = [word_list.count(i) for i in word_list]
	word_dict = dict(zip(word_list, word_count))
	words = list(word_dict.items())
	words.sort(key=lambda tup: tup[1], reverse=True)
	top_ten = [words[i] for i in range(min(10, len(words)))]
	return top_ten
		# print(words[i])

print(get_word_count(word_list))

