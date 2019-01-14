# lab-21-count-words_v2.py

import string

translator = str.maketrans("", "", string.punctuation)
with open('a-modest-proposal.txt') as f:
	word_list = f.read().lower().translate(translator).split()

def get_bigrams(word_list):
	bigram_list = [(word_list[i], word_list[i + 1]) for i in range(len(word_list)-1)]
	# bigram_list = []
	# for i in range(len(word_list)-1):
	# 	bigram_list.append((word_list[i], word_list[i + 1]))
	bigram_count = [bigram_list.count(i) for i in bigram_list]
	bigram_dict = dict(zip(bigram_list, bigram_count))
	bigrams = list(bigram_dict.items())
	bigrams.sort(key=lambda tup: tup[1], reverse=True)
	return [bigrams[i] for i in range(min(10, len(bigrams)))]

print(get_bigrams(word_list))