from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]

def find():
    teachers = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                target = (i, j)
            elif grid[i][j] == 'J':
                start = (i, j)
            elif grid[i][j] == 'T':
                teachers.append((i, j))
    return start, target, teachers

s, t, teachers = find()
target_i, target_j = t

dir = ((1,0), (0,1), (-1,0), (0,-1))


def bfs(start, cost):
    si, sj = start
    q = deque()
    q.append((si,sj))
    visited = [[21e9]*M for _ in range(N)]
    visited[si][sj] = 0
    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != '#' and visited[ni][nj] > visited[i][j] + cost:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + cost
    return visited

dist_j = bfs(s, 2)
dist_s = bfs(t, 1)

res = 21e9
if dist_j[target_i][target_j] !=21e9:
    res = dist_j[target_i][target_j]
for ti, tj in teachers:
    if dist_j[ti][tj] != 21e9 and dist_s[ti][tj] != 21e9:
        total = dist_j[ti][tj] + dist_s[ti][tj]
        if total < res:
            res = total

print(res if res != 21e9 else -1)
