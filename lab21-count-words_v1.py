# lab21-count-words.py

import string

# words to ignore
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
             'you', "you're", "you've", "you'll", "you'd", 'your', 'yours',
             'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
             "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
             'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
             'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
             'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
             'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the',
             'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
             'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
             'through', 'during', 'before', 'after', 'above', 'below', 'to',
             'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
             'again', 'further', 'then', 'once', 'here', 'there', 'when',
             'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
             'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
             'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
             'can', 'will', 'just', 'don', "don't", 'should', "should've",
             'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
             "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn',
             "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't",
             'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't",
             'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn',
             "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# open file, change comma separated string into a list
translator = str.maketrans("", "", string.punctuation)
with open('heart-of-darkness.txt') as f:
	word_list = f.read().lower().translate(translator).split()

# get frequency of word use, return 10 most frequent
def get_word_count(word_list):
    word_count = [word_list.count(i) for i in word_list]
    word_dict = dict(zip(word_list, word_count))
    for i in stopwords:
        if i in word_dict:
            word_dict.pop(i)
    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    top_ten = [words[i] for i in range(min(10, len(words)))]
    return top_ten

print(get_word_count(word_list))

