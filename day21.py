# https://adventofcode.com/2021/day/21

import sys

input_data = sys.stdin.read().strip().splitlines()
start1 = int(input_data[0].split()[-1])
start2 = int(input_data[1].split()[-1])

# Part 1
pos = [start1, start2]
score = [0, 0]
rolls = 0
dice = 1
player = 0
while score[0] < 1000 and score[1] < 1000:
    moves = 0
    for _ in range(3):
        rolls += 1
        moves += dice
        dice = (dice % 100) + 1
    pos[player] = (pos[player] + (moves - 1)) % 10 + 1
    score[player] += pos[player]
    player = (player + 1) % 2
print(rolls * min(score))

# Part 2
seen = {}
def count_wins(pos1, pos2, score1, score2):
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1
    if (pos1, pos2, score1, score2) in seen:
        return seen[(pos1, pos2, score1, score2)]
    wins1, wins2 = 0, 0
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                next_pos = (pos1 + d1 + d2 + d3 - 1) % 10 + 1
                next_score = score1 + next_pos
                w2, w1 = count_wins(pos2, next_pos, score2, next_score)
                wins1 += w1
                wins2 += w2
    seen[(pos1, pos2, score1, score2)] = (wins1, wins2)
    return wins1, wins2
print(max(count_wins(start1, start2, 0, 0)))
