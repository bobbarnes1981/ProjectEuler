
def solution(number):
	i = 0
	j = 2
	while i < number:
		if is_prime(j):
			i+=1
			print('%s\t%s' % (i, j))
		j+=1
	
def is_prime(number):
	left = 2
	right = number
	while left < right:
		right = number/left
		if number % left == 0:
			return False
		left+=1
	return True
	
if __name__ == '__main__':
	solution(10001)