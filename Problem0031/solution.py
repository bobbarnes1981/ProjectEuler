
combinations = 1 * 200 * 2 * 100 * 5 * 40 * 10 * 20 * 20 * 10 * 50 * 4 * 100 * 2 * 200 * 1

coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200

count = 0

def test(output, total, target):
    if sum(total) > target:
        #print('FAIL {0} = {1}'.format(' '.join(output), sum(total)))
        return True
    else:
        #print('FAIL {0} = {1}'.format(' '.join(output), sum(total)))
        return False

for a in range(0, 201):
    total = [1 * a, 0, 0, 0, 0, 0, 0, 0]
    output = ['1 * {0}'.format(a), '', '', '', '', '', '', '']

    for b in range(0, 101):
        total[1] = 2 * b
        output[1] = ' + 2 * {0}'.format(b)

        if test(output[:2], total[:2], target):
            break

        for c in range(0, 41):
            total[2] = 5 * c
            output[2] = ' + 5 * {0}'.format(c)

            if test(output[:3], total[:3], target):
                break

            for d in range(0, 21):
                total[3] = 10 * d
                output[3] = ' + 10 * {0}'.format(d)

                if test(output[:4], total[:4], target):
                    break

                for e in range(0, 11):
                    total[4] = 20 * e
                    output[4] = ' + 20 * {0}'.format(e)

                    if test(output[:5], total[:5], target):
                        break

                    for f in range(0, 5):
                        total[5] = 50 * f
                        output[5] = ' + 50 * {0}'.format(f)

                        if test(output[:6], total[:6], target):
                            break

                        for g in range(0, 3):
                            total[6] = 100 * g
                            output[6] = ' + 100 * {0}'.format(g)

                            if test(output[:7], total[:7], target):
                                break

                            for h in range(0, 2):
                                total[7] = 200 * h
                                output[7] = ' + 200 * {0}'.format(h)

                                if sum(total) == target:
                                    count = count + 1
                                    print('SUCC {0} = {1} ({2})'.format(' '.join(output), target, count))

