numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ensure sorted
numbers.sort()

print(numbers)

count = 0

def recurse(cur, nums):
    if len(nums) == 0:
        global count
        count = count + 1
        print(count, cur)
        if count == 1000000:
            print('done')
            return True
        return False
    for i in range(0, len(nums)):
        cpy = list(nums)
        val = cpy[i]
        del(cpy[i])
        if recurse(cur+str(val), cpy):
            return True

recurse('', numbers)
