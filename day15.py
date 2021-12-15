# https://adventofcode.com/2021/day/15

import sys
import math
from queue import PriorityQueue

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
grid = [[int(x) for x in line] for line in sys.stdin.read().strip().splitlines()]
nrows = len(grid)
ncols = len(grid[0])

# Extend grid to 5x5 for part 2
for _ in range(4):
    for _ in range(nrows):
        grid.append([])
        for c in range(ncols):
            grid[-1].append((grid[len(grid) - nrows - 1][c] % 9) + 1)
for r in range(len(grid)):
    for _ in range(4):
        for _ in range(ncols):
            grid[r].append((grid[r][len(grid[r]) - ncols] % 9) + 1)

# Update dimensions for extended grid
part1_target = (nrows - 1, ncols - 1)
nrows = len(grid)
ncols = len(grid[0])
part2_target = (nrows - 1, ncols - 1)

def valid_pos(r, c):
    return r >= 0 and r < nrows and c >= 0 and c < ncols

visited = set()
dist = {(0, 0): 0}
for r in range(nrows):
    for c in range(ncols):
        if (r, c) != (0, 0):
            dist[(r, c)] = math.inf

Q = PriorityQueue()
Q.put((0, 0, 0))
while not Q.empty():
    d, r, c = Q.get()
    if (r, c) == part1_target:
        print(dist[part1_target])
    if (r, c) == part2_target:
        print(dist[part2_target])
        break
    for dr, dc in dirs:
        r2 = r + dr
        c2 = c + dc
        if valid_pos(r2, c2) and (r2, c2) not in visited:
            alt = d + grid[r2][c2]
            if alt < dist[(r2, c2)]:
                dist[(r2, c2)] = alt
            Q.put((dist[(r2, c2)], r2, c2))
            visited.add((r2, c2))
