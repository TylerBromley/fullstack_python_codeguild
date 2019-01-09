# lab11-simple-calculator_v3.py

# get an arithmetic expression from a user
math_todo = input("Please enter an arithmetic expression: ")

# evaluate the expression using built-in eval() function
# and store it in a variable
evaluated = eval(math_todo)
# print the evaluated answer
print(f"Your answer is: {evaluated}")