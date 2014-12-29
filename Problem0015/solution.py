
def solution(size):
	triangle = []
	for y in range(0, size+1):
		triangle.append([])
		for x in range(0, size+1):
			if x == 0 or y == 0:
				triangle[y].append(1)
			else:
				triangle[y].append(triangle[y-1][x] + triangle[y][x-1])
	print(triangle[-1][-1])
	
if __name__ == '__main__':
	solution(20)