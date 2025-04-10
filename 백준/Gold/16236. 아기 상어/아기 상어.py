from collections import deque
import sys
input=sys.stdin.readline
dir = ((-1, 0), (0, -1), (0, 1),(1, 0) )

def find_shark():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                grid[i][j]=0
                return (i,j)

def bfs(loc):
    q = deque()
    q.append((loc[0], loc[1], 0))  # (i, j, distance)
    visited = [[0] * N for _ in range(N)]
    visited[loc[0]][loc[1]] =1
    fishes = []

    while q:
        ti, tj, dist = q.popleft()
        for d in dir:
            wi, wj = ti + d[0], tj + d[1]
            if 0 <= wi < N and 0 <= wj < N and not visited[wi][wj] and grid[wi][wj] <= shark_size:
                visited[wi][wj] = 1
                if 0 < grid[wi][wj] < shark_size:
                    fishes.append((dist + 1, wi, wj))
                else:
                    q.append((wi, wj, dist + 1))
    if not fishes:
        return -1, 'lost'
    fishes.sort()
    dist, fi, fj = fishes[0]
    grid[fi][fj] = 0
    return dist, (fi, fj)

N = int(input())
grid = list(list(map(int, input().split())) for _ in range(N))
shark_loc = find_shark()
shark_size = 2
cnt = 0
turn = 0
res = 0
while 1:
    # turn은 visited 값을 받아오거나 먹을 물고기가 없으면 -1을 가져옴
    turn, cur_loc = bfs(shark_loc)
    if turn == -1:
        break
    res += turn
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
    shark_loc = cur_loc
print(res)