from collections import deque
import sys
input = sys.stdin.readline

# 상, 하, 북, 남, 동, 서 (z, y, x)
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start = None

    for l in range(L):
        floor = []
        for r in range(R):
            row = list(input().strip())
            for c in range(C):
                if row[c] == 'S':
                    start = (l, r, c)
            floor.append(row)
        input()  # 빈 줄 처리
        building.append(floor)

    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    q = deque()
    q.append((*start, 0))
    visited[start[0]][start[1]][start[2]] = True

    escaped = False

    while q:
        z, y, x, time = q.popleft()

        if building[z][y][x] == 'E':
            print(f"Escaped in {time} minute(s).")
            escaped = True
            break

        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                if not visited[nz][ny][nx] and building[nz][ny][nx] != '#':
                    visited[nz][ny][nx] = True
                    q.append((nz, ny, nx, time + 1))

    if not escaped:
        print("Trapped!")
