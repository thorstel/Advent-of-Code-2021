# https://adventofcode.com/2021/day/18

import sys

def parse_number(line):
    xs = []
    depth = 0
    for c in line:
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        elif c != ',':
            xs.append((depth, int(c)))
    return xs

def find_explosion(xs):
    for i, x in enumerate(xs[:-1]):
        if x[0] > 4 and x[0] == xs[i + 1][0]:
            return i
    return None

def find_split(xs):
    for i, x in enumerate(xs):
        if x[1] > 9:
            return i
    return None

def add_numbers(num1, num2):
    xs = num1 + num2
    for i, x in enumerate(xs):
        xs[i] = (x[0] + 1, x[1])
    return xs

def reduce_number(xs):
    while True:
        expl_idx = find_explosion(xs)
        if expl_idx is not None:
            left = xs[:expl_idx]
            right = xs[expl_idx + 2:]
            if len(left) > 0:
                left[-1] = (left[-1][0], left[-1][1] + xs[expl_idx][1])
            if len(right) > 0:
                right[0] = (right[0][0], right[0][1] + xs[expl_idx + 1][1])
            xs = left + [(xs[expl_idx][0] - 1, 0)] + right
            continue
        split_idx = find_split(xs)
        if split_idx is not None:
            left = xs[:split_idx]
            right = xs[split_idx + 1:]
            depth = xs[split_idx][0] + 1
            lval = xs[split_idx][1] // 2
            rval = lval + (xs[split_idx][1] % 2)
            xs = left + [(depth, lval), (depth, rval)] + right
            continue
        return xs

def calc_magnitude(xs):
    while len(xs) > 1:
        dmax = -1
        for d, x in xs:
            dmax = max(dmax, d)
        for i in range(len(xs) - 1):
            if xs[i][0] == dmax and xs[i + 1][0] == dmax:
                left = xs[:i]
                right = xs[i + 2:]
                xs = left + [(dmax - 1, 3 * xs[i][1] + 2 * xs[i + 1][1])] + right
                break
    return xs[0][1]

# Read input
numbers = [parse_number(line.strip()) for line in sys.stdin.read().splitlines()]

# Part 1
xs = numbers[0]
for number in numbers[1:]:
    xs = reduce_number(add_numbers(xs, number))
print(calc_magnitude(xs))

# Part 2
max_magnitude = -1
for i, x in enumerate(numbers[:-1]):
    for y in numbers[i + 1:]:
        m1 = calc_magnitude(reduce_number(add_numbers(x, y)))
        m2 = calc_magnitude(reduce_number(add_numbers(y, x)))
        max_magnitude = max(max_magnitude, m1, m2)
print(max_magnitude)
