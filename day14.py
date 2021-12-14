# https://adventofcode.com/2021/day/14

import sys
from collections import *

poly, instructions = sys.stdin.read().strip().split('\n\n')
rules = {}
for line in instructions.splitlines():
    x, y = line.split(' -> ')
    rules[x] = y

pair_cnt = Counter()
for i in range(len(poly) - 1):
    pair_cnt[poly[i] + poly[i + 1]] += 1

for step in range(40):
    new_cnt = Counter()
    for pair in pair_cnt:
        new_cnt[pair[0] + rules[pair]] += pair_cnt[pair]
        new_cnt[rules[pair] + pair[1]] += pair_cnt[pair]
    pair_cnt = new_cnt
    if step == 9 or step == 39:
        single_cnt = Counter()
        for pair in pair_cnt:
            single_cnt[pair[0]] += pair_cnt[pair]
        single_cnt[poly[-1]] += 1
        occurrences = single_cnt.most_common()
        print(occurrences[0][1] - occurrences[-1][1])
