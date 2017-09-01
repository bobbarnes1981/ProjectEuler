
numbers = []

def is_pandigital(number):
     l = list(number)
     l.sort()
     return l == list('123456789')

def test():
    global numbers
    for i in range(1, 10000):
        for j in range(2, 10):
            output = ''
            compare = ''
            for k in range(1, j+1):
                num = i * k
                output += '{0} * {1} = {2}\r\n'.format(i, k, num)
                compare += str(num)
            if len(compare) == 9:
                if is_pandigital(compare):
                    print(output)
                    print('\t{0}'.format(compare))
                    numbers.append(int(compare))
            if len(compare) > 9:
                break

test()

numbers.sort()
print(numbers)

