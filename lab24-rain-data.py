# lab24-rain-data.py

import numpy as np
import matplotlib as plt
import datetime
import csv
from matplotlib.dates import datestr2num

with open('hayden_island.rain.txt', 'r') as f:
    stripped = (line.strip() for line in f)
    lines = (line.split(",") for line in stripped if line)
    with open('hayden_island.rain.csv', 'w') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(('date', 'total'))
        writer.writerows(lines)

# print(np.loadtxt('hayden_island.rain.txt', skiprows=2, dtype=np.int_, converters = {0: datestr2num}))
# print(np.genfromtxt('hayden_island.rain.txt', missing_values='missing', skip_header=2))
# arrays = [np.array(map(int, line.split())) for line in open('hayden_island.rain.txt')]
# print(*arrays)

# count = 0
# date = []
# columns = []
# for line in table_data:
#     line = line.strip()
#     columns = line.split()
#     # count += 1
 
# for col in columns:
#     date.append(columns[:1])
    
#     # date_int = []
#     # for i in date:
#     #     date_int.append(datetime.datetime.strptime(i, '%d-%b-%Y'))
#     rain = columns[1:2]
#     # data = dict(zip(date, rain))
#     # if count > 2:
#     #     print(data)
# print(date)
# for k,v in data:


# for i in range(len(columns)):
#     print(columns[0], columns[1])
