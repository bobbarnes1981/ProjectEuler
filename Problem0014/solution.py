
def solution(max):
	s_len = 0
	s_num = 0
	lengths = []
	for i in range(0, max):
		length = 0
		num = i
		while num > 0:
			length += 1
			if num == 1:
				break
			if num % 2 == 0:
				num = num / 2
			else:
				num = (3 * num) + 1
			if num < len(lengths):
				length += lengths[num]
				num = 0
		lengths.append(length)
		if length > s_len:
			s_len = length
			s_num = i
	print('n:%s\tlen:%s' % (s_num, s_len))
	print(len(collatz(s_num)))
	
def collatz(start):
	seq = []
	num = start
	while num > 0:
		seq.append(num)
		if num == 1:
			break
		if num % 2 == 0:
			num = num / 2
		else:
			num = (3 * num) + 1
	return seq
		
if __name__ == '__main__':
	solution(1000000)