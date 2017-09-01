
def is_palindrome(string):
    for i in range(0, len(string) / 2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

total = 0

for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        print('{0} {1}'.format(i, bin(i)[2:]))
        total += i

print('sum: {0}'.format(total))

