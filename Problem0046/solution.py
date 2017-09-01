
maximum = 10000

def sieve(maximum):
    numbers = {}
    primes = []
    for i in range(2, maximum):
        numbers[i] = True
    for number in numbers.keys():
        if numbers[number] == True:
            primes.append(number)
            for j in range(number+number, maximum, number):
                numbers[j] = False
    return primes

primes = sieve(maximum)

def test(primes, target):
    print('target {0}'.format(target))
    for prime in primes:
        if prime + 2 > target:
            return False
        for i in range(1, 1000):
            result = prime + (2 * pow(i, 2))
            if result == target:
                print('{0} = {1} + 2 x pow({2}, 2)'.format(target, prime, i))
                return True
            if result > target:
                break
    return False

# odd composites x = prime + 2*pow(y,z)

for target in range(3, maximum, 2):
    if target not in primes:
        if test(primes, target) == False:
            print('FOUND {0}'.format(target))
            exit()

