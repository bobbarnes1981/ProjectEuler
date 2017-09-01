
numbers = [1,2,3,4,5,6,7,8,9]

answer = []

def find(value):
    for i in range(1, 8):
        for j in range(i+1, 9):
            total = int(value[j:])
            if int(value[:i]) * int(value[i:j]) == total:
                global answer
                if total not in answer:
                    answer.append(total)
                print(len(answer))
                print('{0}x{1}={2}'.format(value[:i], value[i:j], value[j:]))

def recurse(cur, nums):
    if len(nums) == 0:
        #print(cur)
        find(cur)
    for i in range(0, len(nums)):
        cpy = list(nums)
        val = cpy[i]
        del(cpy[i])
        recurse(cur+str(val), cpy)

recurse('', numbers)

print(answer)
print(sum(answer))

