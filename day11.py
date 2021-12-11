# https://adventofcode.com/2021/day/11

import sys

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
grid = [[int(x) for x in line.strip()] for line in sys.stdin]
nrows = len(grid)
ncols = len(grid[0])

def pos_valid(r, c):
    return r >= 0 and r < nrows and c >= 0 and c < ncols

ans1 = 0
ans2 = 0 # number of steps
while True:
    for r in range(nrows):
        for c in range(ncols):
            grid[r][c] += 1
    num_flashes = -1
    has_flashed = []
    while num_flashes != len(has_flashed):
        num_flashes = len(has_flashed)
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] > 9 and (r, c) not in has_flashed:
                    has_flashed.append((r, c))
                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        if pos_valid(nr, nc):
                            grid[nr][nc] += 1
    for r, c in has_flashed:
        grid[r][c] = 0
    if ans2 < 100:
        ans1 += num_flashes
    ans2 += 1
    if num_flashes == nrows * ncols:
        assert ans2 > 100 # part 1 will be wrong if part 2 < 100
        break
print(ans1)
print(ans2)
