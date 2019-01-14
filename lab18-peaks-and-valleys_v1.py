# lab18-peaks-and-valleys.py
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
	peak = []
	for i in range(1, len(data)-1):
		if data[i - 1] < data[i] > data[i + 1]:
			peak.append(i)
	return peak

def valleys(data):
	valley = []
	for i in range(1, len(data)-1):
		if data[i - 1] > data[i] < data[i + 1]:
			valley.append(i)
	return valley

def peaks_and_valleys(data):
	p = peaks(data)
	v = valleys(data)
	p_and_v = p + v
	p_and_v.sort()
	return p_and_v

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
