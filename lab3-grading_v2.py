# lab3-grading_v2.py


user_grade = int(input("Please enter your grade: > "))

if user_grade >= 90 and user_grade <= 100:
    if user_grade > 96:
        print("You got an A+")
    elif user_grade > 93 and user_grade <= 96:
        print("You got an A")
    elif user_grade >= 90:
        print("A-")
elif user_grade >= 80 and user_grade <= 89:
    if user_grade > 86:
        print("You got a B+")
    elif user_grade > 83 and user_grade <= 86:
        print("You got a B")
    elif user_grade >= 80:
        print("B-")
elif user_grade >= 70 and user_grade <= 79:
    if user_grade > 76:
        print("You got a C+")
    elif user_grade > 73 and user_grade <= 76:
        print("You got a C")
    elif user_grade >= 70:
        print("C-")
elif user_grade >= 60 and user_grade <= 69:
    if user_grade > 66:
        print("You got a D+")
    elif user_grade > 63 and user_grade <= 66:
        print("You got a D")
    elif user_grade >= 60:
        print("C-")
elif user_grade >= 0 and user_grade <= 59:
    print("You got an F")
elif user_grade > 100:
    print("Sorry. There's no A++")
else:
    print("That input seems incorrect.")