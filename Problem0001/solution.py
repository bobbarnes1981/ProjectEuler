
def solution(max):
	total = 0
	for i in range(0, max):
		if i % 5 == 0 or i % 3 == 0:
			total += i;
	print(total)

if __name__ == '__main__':
	solution(1000)