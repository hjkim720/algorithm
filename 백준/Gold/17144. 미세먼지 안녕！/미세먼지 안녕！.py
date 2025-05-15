from math import floor
import sys
input=sys.stdin.readline
R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

purifier = []
for r in range(R):
    if grid[r][0] == -1:
        purifier.append((r, 0))
        purifier.append((r + 1, 0))
        break

def activate():
    global grid
    i, j = purifier[0][0] - 1, 0
    while i > 0:
        grid[i][j] = grid[i - 1][j]
        i -= 1
    while j < C - 1:
        grid[i][j] = grid[i][j + 1]
        j += 1
    while i < purifier[0][0]:
        grid[i][j] = grid[i + 1][j]
        i += 1
    while j > 1:
        grid[i][j] = grid[i][j - 1]
        j -= 1
    grid[i][j] = 0


    i, j = purifier[1][0] + 1, 0
    while i < R - 1:
        grid[i][j] = grid[i + 1][j]
        i += 1
    while j < C - 1:
        grid[i][j] = grid[i][j + 1]
        j += 1
    while i > purifier[1][0]:
        grid[i][j] = grid[i - 1][j]
        i -= 1
    while j > 1:
        grid[i][j] = grid[i][j - 1]
        j -= 1
    grid[i][j] = 0

dir = ((1,0),(-1,0),(0,1),(0,-1))

def spread(r, c):
    cnt = 0
    amount = floor(grid[r][c] / 5)
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1:
            new[nr][nc] += amount
            cnt += 1
    new[r][c] += grid[r][c] - cnt * amount

for _ in range(T):
    new = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                spread(i, j)
    new[purifier[0][0]][0] = -1
    new[purifier[1][0]][0] = -1
    grid = new
    activate()

res = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] > 0:
            res += grid[i][j]
print(res)
