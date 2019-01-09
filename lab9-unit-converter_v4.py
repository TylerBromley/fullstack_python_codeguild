# lab9-unit-converter_v4.py

distance = float(input("What is the distance? "))
in_unit = int(input("What is the input unit? Please enter\n\t[1] for feet\n\t" +
                "[2] for miles\n\t[3] for kilometers\n\t[4] for meters\n> "))
out_unit = int(input("What is the output unit? Please enter\n\t[1] for feet\n" +
                "\t[2] for miles\n\t[3] for kilometers\n\t[4] for meters\n> "))


meters = 0

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

convert_to_meters(distance, in_unit)
convert_to_output(out_unit)

units = {
    1 : "ft",
    2 : "mi",
    3 : "km",
    4 : "m",
}

if in_unit in units:
    in_unit = units[in_unit]

if out_unit in units:
    out_unit = units[out_unit]


print(f"{distance} {in_unit} is {meters} {out_unit}")
"""
def convert_meters_to_out_units():
if out_units.startswith("f"):
    meters = round(meters / METER_CONST, 4)
    out_units = "ft"
elif out_units.startswith("mi"):
    meters = round(meters / 5280, 4)
    out_units = "m"

elif out_units.startswith("k"):
    meters = round(meters * 1000, 4)
    out_units = "km"        
else:
    meters = meters
    out_units = "m"


print(f"{int(distance)} {in_units} is {meters} {out_units}")
"""