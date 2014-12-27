
def solution(target):
	left = 2
	right = target
	result = 0
	while left < right:
		if target % left == 0:
			print('%i x %i' % (left, right))
			right = target/left
			if is_prime(right) and right > result:
				result = right
			if is_prime(left) and left > result:
				result = left
		left+=1
	print(result)

def is_prime(number):
	i = 2
	while i < number:
		if number % i == 0:
			return False
		i+=1
	return True
	
if __name__ == '__main__':
	solution(600851475143)