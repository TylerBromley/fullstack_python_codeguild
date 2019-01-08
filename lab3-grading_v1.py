# lab3-grading.py


user_grade = int(input("Please enter your grade: > "))

if user_grade <= 100 and user_grade >= 90:
    print("You got an A!")
elif user_grade < 90 and user_grade >= 80:
    print("You got a B!")
elif user_grade < 80 and user_grade >= 70:
    print("You got a C. Good effort!")
elif user_grade < 70 and user_grade >= 60:
    print("You got a D.")
elif user_grade < 60 and user_grade >= 0:
    print("You fail.")
elif user_grade > 100:
    print("There's no A++.")
#elif user_grade < 0:
#    print("How does one manage that?")
else:
    print("That input seems incorrect.")