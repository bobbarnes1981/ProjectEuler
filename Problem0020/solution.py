import sys
sys.path.append('..')
from bignumber import BigNumber

def solution(number):
	digits = factorial(BigNumber(str(number))).digits
	sum = 0
	for digit in digits:
		sum += digit
	print(sum)

def factorial(number):
	if len(number.digits) == 1 and number.digits[0] == 1:
		return number
	return number * factorial(number-BigNumber('1'))

if __name__ == '__main__':
	solution(100)