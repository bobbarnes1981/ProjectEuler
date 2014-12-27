
def solution():
	result = 0
	for a in range(999, 100, -1):
		for b in range(999, 100, -1):
			number = a * b
			if is_palindrome(number) and number > result:
				result = number
	print(result)

def is_palindrome(number):
	string = str(number)
	for i in range(0, len(string)/2):
		if string[i] != string[len(string)-(1+i)]:
			return False
	return True
	
if __name__ == '__main__':
	solution()