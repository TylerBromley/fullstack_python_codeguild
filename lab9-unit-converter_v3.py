# lab9-unit-converter_v3.py

user_input = float(input("What is the distance? "))
units = input("Please enter the unit (feet, miles, yds, ins, meters, kms): ").strip().lower()
unit_name = ""
meter_num = 0.3048
if (units == "foot") | (units == "feet"):
	meters = round(user_input * meter_num, 4)
	unit_name = "ft"
elif (units == "miles") | (units == "mile"):
	meters = round((user_input * meter_num) * 5280, 4)
	if user_input == 1:
		unit_name = "mile"
	else:
		unit_name = "miles"
elif units.startswith("kilo"):
	meters = round(user_input * 1000, 4)
	if user_input == 1:
		unit_name = "km"
	else:
		unit_name = "kms"
elif units.startswith("m"):
	meters = user_input
	unit_name = "m"
elif units.startswith("y"):
	meters = round(user_input * 0.9144, 4)
	if user_input == 1:
		unit_name = "yd"
	else:
		unit_name = "yds"
elif units.startswith("in"):
	meters = round(user_input * 0.0254, 4)
	unit_name = "in"
else:
	print("that's not a proper unit.")

print(f"{int(user_input)} {unit_name} is {meters} m.")