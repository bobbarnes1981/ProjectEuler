import sys
sys.path.append('..')
from bignumber import BigNumber

def solution(power):
	number = BigNumber('2')
	result = BigNumber('2')
	for i in range(0, power-1):
		result = result * number
	print(result)
	total = 0
	for number in str(result):
		total += int(number)
	print(total)

if __name__ == '__main__':
	solution(1000)