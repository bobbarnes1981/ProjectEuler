
def solution(length):
	f = open('data.txt', 'r+')
	data = f.read()
	f.close()
	data = data.split('\n')
	for i in range(0, len(data)):
		numbers = data[i].split(' ')
		data[i] = []
		for number in numbers:
			data[i].append(int(number))
	w = len(data[0])
	h = len(data)
	print('%s, %s' % (w, h))
	result = 0
	for y in range(0, h):
		for x in range(0, w):
			#row
			if x < w - length:
				r_prod = data[y][x]
				for i in range(1, length):
					r_prod *= data[y][x+i]
				if r_prod > result:
					result = r_prod
			#col
			if y < h - length:
				c_prod = data[y][x]
				for i in range(1, length):
					c_prod *= data[y+i][x]
				if c_prod > result:
					result = c_prod
			#diags
			if x < w - length and y < h - length:
				r_prod = data[y][x]
				l_prod = data[y][x+length]
				for i in range(1, length):
					r_prod *= data[y+i][x+i]
					l_prod *= data[y+i][x+length-i]
				if r_prod > result:
					result = r_prod
				if l_prod > result:
					result = l_prod
	print(result)

if __name__ == '__main__':
	solution(4)