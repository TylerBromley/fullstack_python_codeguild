# lab9-unit-converter_v4.py

# get the user's distance, sans unit of measure
distance = float(input("What is the distance? "))
# ask for in an out units, but restrict the way they can be entered to numbers
in_unit = int(input("What is the input unit? Please enter\n\t[1] for feet\n\t" +
                "[2] for miles\n\t[3] for kilometers\n\t[4] for meters\n> "))
out_unit = int(input("What is the output unit? Please enter\n\t[1] for feet\n" +
                "\t[2] for miles\n\t[3] for kilometers\n\t[4] for meters\n> "))

# create a global meters variable
meters = 0

# convert the input to meters
def convert_to_meters(distance, in_unit):
    global meters
    if in_unit == 1:
        meters = round(distance * 0.3048, 4)
    elif in_unit == 2:
        meters = round(distance * 1609.344, 4)
    elif in_unit == 3:
        meters = round(distance * 1000, 4)
    elif in_unit == 4:
        meters = distance

# convert the output to the user's chosen unit of measure
def convert_to_output(out_unit):
    global meters
    if out_unit == 1:
        meters = round(meters / 0.3048, 4)
    elif out_unit == 2:
        meters = round(meters / 1609.344, 4)
    elif out_unit == 3:
        meters = round(meters / 1000, 4)
    elif out_unit == 4:
        meters = meters

# call the functions
convert_to_meters(distance, in_unit)
convert_to_output(out_unit)

# create a unit dictionary for printing
units = {
    1 : "ft",
    2 : "mi",
    3 : "km",
    4 : "m",
}

# set in_unit and out_unit to string from units dictionary
if in_unit in units:
    in_unit = units[in_unit]

if out_unit in units:
    out_unit = units[out_unit]

# print the conversion
print(f"{distance} {in_unit} is {meters} {out_unit}")



