
def solution(number):
	sum_square = 0
	square_sum = 0
	for i in range(1, number+1):
		sum_square += pow(i, 2)
		square_sum += i
	square_sum = pow(square_sum, 2)
	print(square_sum - sum_square)
	
if __name__ == '__main__':
	solution(100)