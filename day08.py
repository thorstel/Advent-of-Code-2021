# https://adventofcode.com/2021/day/8

from itertools import permutations
import sys

valid = { 'abcefg':  0,
          'cf':      1,
          'acdeg':   2,
          'acdfg':   3,
          'bcdf':    4,
          'abdfg':   5,
          'abdefg':  6,
          'acf':     7,
          'abcdefg': 8,
          'abcdfg':  9 }

def is_valid(trans, xs):
    for x in xs:
        y = "".join(sorted(map(lambda s: trans[s], x)))
        if y not in valid:
            return False
    return True

perms = [''.join(p) for p in permutations('abcdefg')]
ans1 = 0
ans2 = 0
for line in sys.stdin:
    patterns = line.strip().split(' | ')[0].split()
    outputs = line.strip().split(' | ')[1].split()

    # Part 1
    for out in outputs:
        x = len(out)
        if x == 2 or x == 3 or x == 4 or x == 7:
            ans1 += 1

    # Part 2
    for p in perms:
        trans = dict(zip(p, 'abcdefg'))
        if is_valid(trans, patterns + outputs):
            val = 0
            for out in outputs:
                x = valid["".join(sorted(map(lambda s: trans[s], out)))]
                val = (val * 10) + x
            ans2 += val
            break

print(ans1)
print(ans2)
