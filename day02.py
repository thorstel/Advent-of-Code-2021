# https://adventofcode.com/2021/day/2

import fileinput

pos1, depth1 = 0, 0
pos2, depth2, aim = 0, 0, 0

for line in fileinput.input():
    xs = line.strip().split()
    op, x = xs[0], int(xs[1])
    if op == 'forward':
        pos1 += x
        pos2 += x
        depth2 += aim * x
    elif op == 'down':
        depth1 += x
        aim += x
    elif op == 'up':
        depth1 -= x
        aim -= x
    else:
        assert False

print(pos1 * depth1)
print(pos2 * depth2)
