from collections import deque
import sys
input=sys.stdin.readline


dir = ((0,1), (1,0), (0,-1), (-1,0))

def bfs(x, y):
    global visited
    q = deque()
    q.append((x, y))
    union = [(x, y)]
    visited[x][y] = 1
    total = grid[x][y]

    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if L <= abs(grid[i][j] - grid[ni][nj]) <= R:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    union.append((ni, nj))
                    total += grid[ni][nj]
    return union, total
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
days = 0

while True:
    visited = [[0]*N for _ in range(N)]
    move = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, total = bfs(i, j)
                if len(union) > 1:
                    move = True
                    avg = total // len(union)
                    for x, y in union:
                        grid[x][y] = avg

    if not move:
        break
    days += 1

print(days)
