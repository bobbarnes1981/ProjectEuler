
def solution(max):
	data = {}
	for i in range(1, max):
		result = d(i)
		data[i] = result
	amicable = []
	for key in data.keys():
		result = data[key]
		if result != key:
			if result in data.keys() and data[result] == key:
				amicable.append(key)
				print('%s\t%s' % (key, result))
	print(sum(amicable))

def d(n):
	sum = 0
	devisors = get_devisors(n)
	for devisor in devisors:
		sum += devisor
	return sum
	
def get_devisors(number):
	left = 1
	right = number
	devisors = []
	while left < right:
		if number % left == 0:
			right = number/left
			if left not in devisors:
				devisors.append(left)
			if right not in devisors:
				devisors.append(right)
		left+=1
	devisors.sort()
	return devisors[:-1]

if __name__ == '__main__':
	solution(10000)