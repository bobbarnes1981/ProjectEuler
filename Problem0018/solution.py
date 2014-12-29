
def solution():
	f = open('data.txt', 'r+')
	data = f.read()
	f.close()
	
	data = data.split('\n')
	for i in range(0, len(data)):
		numbers = data[i].split(' ')
		data[i] = []
		for number in numbers:
			data[i].append(int(number))
	
	for row in data:
		print(row)
		
	results = navigate(data, 0, 0, 0)
	print(max(results))

def navigate(data, x, y, total):
	result = []
	number = data[y][x]
	if y == len(data) - 1:
		result.append(total + number)
	else:
		result.extend(navigate(data, x, y+1, total + number))
		result.extend(navigate(data, x+1, y+1, total + number))
	return result
		
if __name__ == '__main__':
	solution()