
letters = {
	'A' : 1,
	'B' : 2,
	'C' : 3,
	'D' : 4,
	'E' : 5,
	'F' : 6,
	'G' : 7,
	'H' : 8,
	'I' : 9,
	'J' : 10,
	'K' : 11,
	'L' : 12,
	'M' : 13,
	'N' : 14,
	'O' : 15,
	'P' : 16,
	'Q' : 17,
	'R' : 18,
	'S' : 19,
	'T' : 20,
	'U' : 21,
	'V' : 22,
	'W' : 23,
	'X' : 24,
	'Y' : 25,
	'Z' : 26,
}

def solution():
	f = open('names.txt', 'r+')
	data = f.read()
	f.close()
	data = data.split(',')
	for i in range(0, len(data)):
		data[i] = data[i].strip('"')
	data.sort()
	total = 0
	for i in range(0, len(data)):
		sum = 0
		for char in data[i]:
			sum += letters[char]
		total += sum * (i + 1)
	print(total)
	
if __name__ == '__main__':
	solution()