# lab18-peaks-and-valleys_v3.py

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data.reverse()
# def peaks(data):
#   peak = []
#   for i in range(1, len(data)-1):
#       if data[i - 1] < data[i] > data[i + 1]:
#           peak.append(i)
#   return peak

# def draw(data):
#   mountain = []
#   peak = max(heights)
#   while peak > 0:
#       row = ['X' if height >= peak else ' ' for height in data]
#       moutain.append("".join(row))
#       peak -= 1
#   return '\n'.join(mountain)


def print_x(data):
    max_of_data = max(data)
    values = []
    line = ""
    has_one = False

    for i in range(10):
        for j in data:
            if j in values:
                line += " X "
                has_one = True
            elif has_one:
                line += " O "
            else:
                line += "   "
        has_one = False
        values.append(max_of_data)
        max_of_data -= 1
        print(line + "\n")
        line = ""

print_x(data)

# def draw_water(data):
#   p = [0] + peaks(data) + [-1]
#   mountain = []
#   peak = max(data)
#   water_height = 0
#   row = []
#   while peak > 0:
#       for i in range(len(data)):
#           if i in p:
#               peak_idx = p.index(i)
#               next_peak_idx = p[peak_idx + 1]
#               if data[i] < data[next_peak_idx]:
#                   water_height = data[i]


#           if i in peak:
#           height = heights[i]
#           if height >= peak:
#               row.append("X")
#           else:

#       row = ['X' if height >= peak else ' ' for height in data]
#       moutain.append("".join(row))
#       peak -= 1
#   return '\n'.join(mountain)
