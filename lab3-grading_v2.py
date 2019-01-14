# lab3-grading_v2.py

# get the letter grade for the number
def letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# find whether the grade has a qualifier
def plus_or_minus(number):
    digit = number % 10
    if digit < 3:
        return '-'
    elif digit > 7:
        return '+'
    else:
        return ''

# append any qualifiers to grade, unless grade is 'F'
def final_grade(number):
    letter = letter_grade(number) 
    modifier = plus_or_minus(number)
    if number > 100 or number < 0:
        print("That's impossible!")
    if letter == 'F':
        return letter
    else:
        return letter + modifier

user_input = int(input("Please enter your grade: "))

print(final_grade(user_input))


