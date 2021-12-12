# https://adventofcode.com/2021/day/12

import sys
from collections import *

caves = defaultdict(list)

for line in sys.stdin:
    xs = line.strip().split('-')
    caves[xs[0]].append(xs[1])
    caves[xs[1]].append(xs[0])

def count_paths(path):
    cnt1 = 0
    cnt2 = 0
    for cave in caves[path[-1]]:
        if cave == 'end':
            cnt1 += 1
            cnt2 += 1
            continue
        elif cave == 'start':
            continue
        if not cave.islower() or cave not in path:
            x, y = count_paths(path + [cave])
            cnt1 += x
            cnt2 += y
        elif not any(x.islower() and path.count(x) > 1 for x in path):
            _, y = count_paths(path + [cave])
            cnt2 += y
    return cnt1, cnt2

ans1, ans2 = count_paths(['start'])
print(ans1)
print(ans2)
