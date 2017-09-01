
def is_palindrome(string):
    for i in range(0, len(string) / 2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

def reverse(string):
    output = ''
    for i in range(len(string)-1, -1, -1):
        output += string[i]    
    return output

def is_lychrel(number):
    current = str(number)
    for i in range(0, 50):
        current = str(int(current) + int(reverse(current)))
        if is_palindrome(current):
            return False
    return True

count = 0
for i in range(0, 10000):
    if is_lychrel(i):
        count+=1
        print('{0} {1}'.format(count, i))

