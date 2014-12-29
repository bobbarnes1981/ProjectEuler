	
class BigNumber(object):

	def __init__(self, number = ''):
		self.digits = []
		for digit in number:
			self.digits.append(int(digit))
		self.digits.reverse()
	
	def __add__(a, b):
		result = []
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
				result.append(int(str(sum)[-1:]))
			else:
				carry = 0
				result.append(sum)
		if carry != 0:
			for digit in str(carry):
				result.append(int(digit))
		result.reverse()
		return BigNumber(''.join(str(x) for x in result).lstrip('0'))

	def __sub__(a, b):
		result = []
		i = 0
		while i < len(a) or i < len(b):
			a_num = 0
			if i < len(a):
				a_num = a.digits[i]
			b_num = 0
			if i < len(b):
				b_num = b.digits[i]
			res = a_num - b_num
			if res < 0:
				j = 1
				while a.digits[i+j] < 1:
					j+=1
				for k in range(j, 0, -1):
					a.digits[i+k] -= 1
					a.digits[i+k-1] += 10
				res = a.digits[i] - b.digits[i]
			result.append(res)
			i+=1
		result.reverse()
		return BigNumber(''.join(str(x) for x in result).lstrip('0'))
		
	def __mul__(a, b):
		a_dig = list(a.digits)
		a_dig.reverse()
		b_dig = list(b.digits)
		b_dig.reverse()
		lattice = Lattice(a_dig, b_dig)
		result = lattice.calculate()
		return BigNumber(''.join(str(x) for x in result).lstrip('0'))

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