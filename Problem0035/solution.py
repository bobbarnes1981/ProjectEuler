
def get_primes(maximum):
    numbers = {}
    primes = []
    for i in range(2, maximum):
        numbers[i] = True
    for number in numbers.keys():
        if numbers[number] == True:
            primes.append(number)
            for i in range(number+number, maximum, number):
                numbers[i] = False
    return primes

def rotate(number):
    output = []
    string = list(str(number))
    for i in range(0, len(string)):
        rotated = string[1:] + string[:1]
        output.append(int(''.join(rotated)))
        string = rotated
    return output

def in_list(items_to_find, list_to_check):
    for item in items_to_find:
        if item not in list_to_check:
            return False
    return True

def get_circular(primes):
    numbers = {}
    circular = []
    for prime in primes:
        numbers[prime] = None
    for number in numbers.keys():
        if numbers[number] == None:
            rotations = rotate(number)
            if in_list(rotations, primes):
                print(rotations)
                for rotation in rotations:
                    if rotation not in circular:
                        circular.append(rotation)
                    numbers[rotation] = True
            else:
                for rotation in rotations:
                    if rotation in numbers:
                        numbers[rotation] = False
    return circular


primes = get_primes(1000000)
circular = get_circular(primes)

print(circular)
print(len(circular))

