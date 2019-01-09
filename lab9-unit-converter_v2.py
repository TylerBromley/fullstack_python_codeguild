# lab9-unit-converter_v2.py

# get the user's distance as float
user_input = float(input("What is the distance? "))
# get the user's unit of measure
units = input("Please enter the unit (feet, miles, meters, kms): ").strip().lower()
# store the unit name for printing
unit_name = ""
# set up a constant for dividing meters
meter_num = 0.3048
# convert the units and set their unit_name
if (units == "foot") | (units == "feet"):
	meters = round(user_input * meter_num, 4)
	unit_name = "ft"
elif (units == "miles") | (units == "mile"):
	meters = round((user_input * meter_num) * 5280, 4)
	if user_input == 1:
		unit_name = "mile"
	else:
		unit_name = "miles"
elif units.startswith("k"):
	meters = round(user_input * 1000, 4)
	if user_input == 1:
		unit_name = "km"
	else:
		unit_name = "kms"
elif units.startswith("me"):
	meters = user_input
	unit_name = "m"
else:
	print("that's not a proper unit.")

# print the conversion
print(f"{int(user_input)} {unit_name} is {meters} m.")