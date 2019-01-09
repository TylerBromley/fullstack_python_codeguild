# lab9-Unit-Converter_v1.py

# get the distance in feet
feet = float(input("What is the distance in feet? "))

# convert the feet to meters, rounded to the fourth place
meters = round(feet * 0.3048, 4)

# print the result
print(f"{int(feet)} ft is {meters} m.")