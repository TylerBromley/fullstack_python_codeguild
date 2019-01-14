# lab18-peaks-and-valleys.py
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak = []
valley = []

def peaks(data):
	prev = 0
	last = 0
	for i in range(len(data)):
		if (last > prev and last > data[i]):
			peak.append(i - 1)
		prev = last
		last = data[i]
	return peak

def valleys(data):
	prev = 0
	last = 0
	for i in range(len(data)):
		if (last < prev and last < data[i]):
			valley.append(i - 1)
		prev = last
		last = data[i]
	return valley

def peaks_and_valleys(peak, valley):
	p_and_v = peak + valley
	p_and_v.sort()
	return p_and_v


print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(peak, valley))
