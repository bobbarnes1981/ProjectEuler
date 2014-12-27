
def solution(length):
	f = open('data.txt', 'r+')
	data = f.read().replace('\r', '').replace('\n', '')
	f.close()
	result = 0
	for i in range(0, len(data) - (length + 1)):
		sum = 0
		for j in range(0, length):
			if sum == 0:
				sum = int(data[i + j])
			else:
				sum *= int(data[i + j])
		if sum > result:
			result = sum
	print(result)
	
if __name__ == '__main__':
	solution(13)