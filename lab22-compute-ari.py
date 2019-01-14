# lab22-compute-ari.py
import re

with open("gettysburg-address.txt") as f:
    text = f.read()

text = re.sub(r'(M\w{1,2})\.', r'\1', text).replace("\n", "")
words = text.split()
letters = []
for word in words:
    for j in word:
        letters.append(j)

print(letters)
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
for i in range(len(words)):
    if words[i].endswith("-"):
        words[i] += words[i + 1]

print(words)
words = words

ari = round(4.71 * (len(letters) / len(words)) + (0.5 * (len(words) /
            len(sentences)) - 21.43))
print(ari)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

for k, v in ari_scale.items():
    if k == ari:
        temp = ari_scale.get(k, v)
        print(f"The ARI for gettysburg-address.txt is {ari}.")
        print(f"This corresponds to a(n) {temp['grade_level']} level of difficulty.")
        print(f"That is suitable for an average person {temp['ages']} years old.")
