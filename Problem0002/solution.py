
def solution(max):
	pre_number = 1
	cur_number = 2
	sum = 0
	while cur_number < max:
		if cur_number % 2 == 0:
			sum += cur_number
		new_number = pre_number + cur_number
		pre_number = cur_number
		cur_number = new_number
	print(sum)

if __name__ == '__main__':
	solution(4000000)