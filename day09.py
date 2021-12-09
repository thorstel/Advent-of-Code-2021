# https://adventofcode.com/2021/day/9

import sys

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
grid = [[int(x) for x in line.strip()] for line in sys.stdin]

nrows = len(grid)
ncols = len(grid[0])

def is_low_point(row, col):
    for (dr, dc) in dirs:
        r = row + dr
        c = col + dc
        if r < 0 or r >= nrows or c < 0 or c >= ncols:
            continue
        if grid[row][col] >= grid[r][c]:
            return False
    return True

# Part 1
ans1 = 0
for r in range(nrows):
    for c in range(ncols):
        if is_low_point(r, c):
            ans1 += 1 + grid[r][c]
print(ans1)

# Part 2
def basin_size(row, col):
    Q = [(row, col)]
    size = 0
    while len(Q) > 0:
        (r, c) = Q.pop(0)
        if grid[r][c] == 9:
            continue
        size += 1
        grid[r][c] = 9
        for (dr, dc) in dirs:
            nr = r + dr
            nc = c + dc
            if nr >= 0 and nr < nrows and nc >= 0 and nc < ncols:
                Q.append((nr, nc))
    return size

sizes = []
for r in range(nrows):
    for c in range(ncols):
        sizes.append(basin_size(r, c))
sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
