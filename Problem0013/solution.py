
def solution():
	f = open('data.txt', 'r+')
	data = f.read()
	f.close()
	data = data.split('\n')
	total = BigNumber()
	for i in range(0, len(data)):
		total += BigNumber(data[i])
	print(str(total))
	print(str(total)[:10])

class BigNumber(object):

	def __init__(self, number = ''):
		self.digits = []
		for digit in number:
			self.digits.append(int(digit))
		self.digits.reverse()
	
	def __add__(a, b):
		output = BigNumber()
		i = 0
		carry = 0
		while i < len(a) or i < len(b):
			sum = carry
			if i < len(a):
				sum += a.digits[i]
			if i < len(b):
				sum += b.digits[i]
			i += 1
			if sum > 9:
				carry = int(sum/10)
				output.digits.append(int(str(sum)[-1:]))
			else:
				carry = 0
				output.digits.append(sum)
		if carry != 0:
			for digit in str(carry):
				output.digits.append(int(digit))
		return output

	def __len__(self):
		return len(self.digits)
		
	def __str__(self):
		output = ''
		for i in range(len(self.digits), 0, -1):
			output += str(self.digits[i-1])
		return output
	
if __name__ == '__main__':
	solution()