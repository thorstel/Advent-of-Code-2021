# https://adventofcode.com/2021/day/20

import sys
from collections import *
from operator import *

alg, img = sys.stdin.read().strip().split('\n\n')
img = img.splitlines()

# Assumption of alternating pixels in infinite image relies on this input property.
assert alg[0] == '#'

trans = {}
for i, x in enumerate(alg.strip()):
    trans[i] = x == '#'

image = defaultdict(bool)
for r, row in enumerate(img):
    for c, x in enumerate(row):
        image[(r, c)] = x == '#'

def get_index(r, c):
    i = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            i <<= 1
            i += 1 if image[(r + dr, c + dc)] else 0
    return i

minrow = -3
maxrow = len(img) + 3
mincol = -3
maxcol = len(img[0]) + 3
for step in range(50):
    if step % 2 == 0:
        new_image = defaultdict(lambda: True)
    else:
        new_image = defaultdict(lambda: False)
    for r in range(minrow, maxrow + 1):
        for c in range(mincol, maxcol + 1):
            new_image[(r, c)] = trans[get_index(r, c)]
    minrow -= 3
    maxrow += 3
    mincol -= 3
    maxcol += 3
    image = new_image

    # Part 1
    if step == 1:
        print(countOf(image.values(), True))

# Part 2
print(countOf(image.values(), True))
