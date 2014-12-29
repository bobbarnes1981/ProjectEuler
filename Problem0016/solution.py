
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
		
	def __mul__(a, b):
		a_dig = list(a.digits)
		a_dig.reverse()
		b_dig = list(b.digits)
		b_dig.reverse()
		lattice = Lattice(a_dig, b_dig)
		result = lattice.calculate()
		return BigNumber(''.join(str(x) for x in result).strip('0'))

	def __len__(self):
		return len(self.digits)
		
	def __str__(self):
		output = ''
		for i in range(len(self.digits), 0, -1):
			output += str(self.digits[i-1])
		return output

class Lattice(object):

	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.data = []
		for y in range(0, len(b)*2, 2):
			self.data.append([])
			self.data.append([])
			for x in range(0, len(a)*2, 2):
				self.data[y].append(None)
				self.data[y].append(None)
				self.data[y+1].append(None)
				self.data[y+1].append(None)
								
				sum = a[x/2] * b[y/2]
				if sum > 9:
					self.data[y][x] = sum / 10
					self.data[y+1][x+1] = int(str(sum)[-1])
				else:
					self.data[y][x] = 0
					self.data[y+1][x+1] = sum
	
	def calculate(self):
		result = []
		for x in range((len(self.a)*2)-1, -1, -2):
			y = (len(self.b)*2)-1
			sum = self.sum_diagonal(x, y)
			if sum > 9:
				carry = sum / 10
				sum = int(str(sum)[-1])
				self.data[y-1][x-1] += carry
			result.append(sum)
		for y in range((len(self.b)*2)-2, -1, -2):
			x = 0
			sum = self.sum_diagonal(x, y)
			if sum > 9:
				carry = sum / 10
				sum = int(str(sum)[-1])
				self.data[y-2][x] += carry
			result.append(sum)
		result.reverse()
		return result
			
	def sum_diagonal(self, start_x, start_y):
		x = start_x
		y = start_y
		sum = 0
		while x < len(self.a)*2 and y > -1:
			sum += self.data[y][x]
			x+=1
			y-=1
		return sum

if __name__ == '__main__':
	solution(1000)