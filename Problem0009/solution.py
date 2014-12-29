import math

def solution(target):
	for a in range(1, target):
		for b in range(a, target):
			c = math.sqrt(pow(a, 2) + pow(b, 2))
			if a + b + c == target:
				print(a * b *c)
				break
	
if __name__ == '__main__':
	solution(1000)