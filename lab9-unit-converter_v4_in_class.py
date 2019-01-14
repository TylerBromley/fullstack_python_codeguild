# lab9-unit-converter_v4_in_class.py

units_in_meters = {
    'mi': 1609.34,
    'ft': 0.3048,
    'km': 1000,
    'm': 1,
    'yd': 0.9144,
    'in': 0.0254
}

def standardized_units():
	if input_units in []:
		pass


def to_meters(distance, units):
    return distance * units_in_meters[units]

def from_meters(distance, units):
    return distance / units_in_meters[units]

def main():
    distance = float(input("Enter your distance: "))
    while True:
    	try:
    		distance = float(input("Enter your distance: "))
    		break
    	except ValueError as e:
    		pass

    while True:
    	try:
    		input_units = input("Enter your units: ")
    		if input_units:
    			break
    	except ValueError:
    		pass
    while True:
    	try:
    		target_units = input("Enter your target units: ")
    		if target_units:
    			break
    	except ValueError:
    		pass	
    
    distance_to_meters = to_meters(distance, input_units)
    meters_to_units = from_meters(distance_to_meters, target_units)

    print(f"{distance} {input_units} {round(distance_to_meters, 4)} {target_units}")

main()