# https://adventofcode.com/2021/day/13

import sys

coords, instructions = sys.stdin.read().strip().split('\n\n')
dots = set()
for line in coords.splitlines():
    x, y = line.split(',')
    dots.add((int(x), int(y)))

def fold_dots(dots, d, f):
    folded = set()
    for x, y in dots:
        assert d == 'x' or d == 'y'
        if d == 'x' and x > f:
            folded.add((2 * f - x, y))
        elif d == 'y' and y > f:
            folded.add((x, 2 * f - y))
        else:
            folded.add((x, y))
    return folded

instr = instructions.splitlines()
for i in range(len(instr)):
    d, f = instr[i].split('=')
    dots = fold_dots(dots, d[-1], int(f))
    if i == 0:
        print(len(dots))

nrows = 0
ncols = 0
for x, y in dots:
    nrows = max(nrows, y)
    ncols = max(ncols, x)

for y in range(nrows + 1):
    for x in range(ncols + 1):
        print('#' if (x, y) in dots else '.', end='')
    print()
