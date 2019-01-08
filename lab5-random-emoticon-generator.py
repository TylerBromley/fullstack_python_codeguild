# lab5-random-emotiocon-generator.py

import random

# lists of face components
eyes_list = [':', ';', 'B', '8']
nose_list = ['\'', '-']
mouth_list = [')', '(', '/']

# the face will be built in emoticon face
emoticon_face = ''

# creates a random face
emoticon_face = emoticon_face + random.choice(eyes_list)
emoticon_face = emoticon_face + random.choice(nose_list)
emoticon_face = emoticon_face + random.choice(mouth_list)

# prints the face
print(emoticon_face)