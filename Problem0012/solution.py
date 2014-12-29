
def solution(target):
	i = 1
	number = 0
	devisors = []
	while len(devisors) < target:
		number += i
		devisors = get_devisors(number)
		print('%s\t%s' % (number, len(devisors)))
		i += 1

def get_devisors(number):
	left = 1
	right = number
	devisors = []
	while left < right:
		if number % left == 0:
			right = number/left
			devisors.append(left)
			devisors.append(right)
		left+=1
	devisors.sort()
	return devisors
		
if __name__ == '__main__':
	solution(500)