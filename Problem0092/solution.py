
maximum = 10000000

ENDS_89 = 89
ENDS_01 = 1
UNKNOWN = 0

count = 0
numbers = {}
for i in range(1, maximum):
    numbers[i] = UNKNOWN

def add(number, chain):
    global numbers
    if number == 89 or numbers[number] == ENDS_89:
        for c in chain:
            numbers[c] = ENDS_89
        return True
    if number == 1 or numbers[number] == ENDS_01:
        for c in chain:
            numbers[c] = ENDS_01
        return False
    total = 0
    string = str(number)
    for digit in string:
        total += pow(int(digit), 2)
    return add(total, chain + [total])

import time
for i in range(1, maximum):
    #print(i)
    if add(i, [i]) == True:
        count += 1
        print('{0}\t{1}'.format(i, count))
print(count)

