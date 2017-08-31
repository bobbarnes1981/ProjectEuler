
def fib_rec(count, prev_num, curr_num, end):
    count = count + 1
    next_num = prev_num + curr_num
    l = len(str(curr_num))
    print(count, l, curr_num)
    if l < end:
        fib_rec(count, curr_num, next_num, end)

def fib_loop(count, prev_num, curr_num, end):
    while True:
        count = count + 1
        next_num = prev_num + curr_num
        l = len(str(curr_num))
        print(count, l, curr_num)
        if l == end:
            break
        prev_num = curr_num
        curr_num = next_num

fib_loop(0, 0, 1, 1000)

