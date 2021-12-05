# https://adventofcode.com/2021/day/5

from collections import *
import sys

field = defaultdict(int)
diagonals = []

for line in sys.stdin:
    xs = line.strip().split(' -> ')
    xy1 = xs[0].split(',')
    x1, y1 = int(xy1[0]), int(xy1[1])
    xy2 = xs[1].split(',')
    x2, y2 = int(xy2[0]), int(xy2[1])
    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            field[(i, y1)] += 1
    elif x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            field[(x1, i)] += 1
    else:
        diagonals.append((x1, y1, x2, y2))

# Part 1
print(sum(1 if x > 1 else 0 for x in field.values()))

# Part 2
for (x1, y1, x2, y2) in diagonals:
    x, y = x1, y1
    field[(x, y)] += 1
    while (x, y) != (x2, y2):
        x += 1 if x < x2 else -1
        y += 1 if y < y2 else -1
        field[(x, y)] += 1
print(sum(1 if x > 1 else 0 for x in field.values()))
