import sys
sys.path.append('..')
from bignumber import BigNumber

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
	
if __name__ == '__main__':
	solution()