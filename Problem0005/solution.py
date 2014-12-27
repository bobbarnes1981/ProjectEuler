
def solution(number):
	i = number
	while True:
		if is_divisible(i, number):
			print(i)
			break
		i+=number

def is_divisible(start, number):
	if number == 1:
		return True
	if start % number == 0:
		return is_divisible(start, number - 1)
	return False
	
if __name__ == '__main__':
	solution(20)