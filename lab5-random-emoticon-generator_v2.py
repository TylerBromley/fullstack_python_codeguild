# lab5-random-emoticon-generator.py

import random

# lists of face components
eyes_list = [':', ';', 'B', '8']
nose_list = ['^', '-']
mouth_list = [')', '(', '/']

# the face will be built in emoticon face
emoticon_face = ''
count = 0

# creates five random faces, one per line
while count < 5:
	emoticon_face = emoticon_face + random.choice(eyes_list)
    emoticon_face = emoticon_face + random.choice(nose_list)
    emoticon_face = emoticon_face + random.choice(mouth_list) + '\n'

    count += 1

# prints out the five faces
print(emoticon_face)