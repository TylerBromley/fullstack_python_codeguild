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

# print(final_grade(98))
# print(final_grade(97))
# print(final_grade(72))
# print(final_grade(65))
# print(final_grade(52))
# print(final_grade(32))
print(final_grade(user_input))

# user_grade = int(input("Please enter your grade: > "))

# if user_grade >= 90 and user_grade <= 100:
#     if user_grade > 96:
#         print("You got an A+")
#     elif user_grade > 93 and user_grade <= 96:
#         print("You got an A")
#     elif user_grade >= 90:
#         print("A-")
# elif user_grade >= 80 and user_grade <= 89:
#     if user_grade > 86:
#         print("You got a B+")
#     elif user_grade > 83 and user_grade <= 86:
#         print("You got a B")
#     elif user_grade >= 80:
#         print("B-")
# elif user_grade >= 70 and user_grade <= 79:
#     if user_grade > 76:
#         print("You got a C+")
#     elif user_grade > 73 and user_grade <= 76:
#         print("You got a C")
#     elif user_grade >= 70:
#         print("C-")
# elif user_grade >= 60 and user_grade <= 69:
#     if user_grade > 66:
#         print("You got a D+")
#     elif user_grade > 63 and user_grade <= 66:
#         print("You got a D")
#     elif user_grade >= 60:
#         print("C-")
# elif user_grade >= 0 and user_grade <= 59:
#     print("You got an F")
# elif user_grade > 100:
#     print("Sorry. There's no A++")
# else:
#     print("That input seems incorrect.")

