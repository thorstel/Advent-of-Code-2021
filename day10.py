# https://adventofcode.com/2021/day/10

import sys

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
p1_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
p2_points = {')': 1, ']': 2, '}': 3, '>': 4}

ans1 = 0
ans2 = []
for line in sys.stdin:
    stack = []
    is_incomplete = True
    for x in line.strip():
        if x == '(' or x == '[' or x == '{' or x == '<':
            stack.append(pairs[x])
        elif len(stack) > 0 and stack[-1] == x:
            stack.pop()
        else:
            ans1 += p1_points[x]
            is_incomplete = False
            break
    # Part 2
    if is_incomplete:
        score = 0
        while len(stack) > 0:
            score = (score * 5) + p2_points[stack[-1]]
            stack.pop()
        ans2.append(score)

print(ans1)
ans2.sort()
print(ans2[len(ans2) // 2])
