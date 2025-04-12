from collections import deque
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs():
    visited = [[[[0] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = deque()
    # (i, j, dir, cut_count, ops)
    q.append((si, sj, 0, 0, 0))
    visited[si][sj][0][0] = 1

    while q:
        i, j, dir, cuts, ops = q.popleft()
        if (i, j) == (ei, ej):
            return ops
        # 전진
        di, dj = d[dir]
        wi, wj = i + di, j + dj
        if 0 <= wi < N and 0 <= wj < N:
            cell = grid[wi][wj]
            if cell in ('G', 'Y') and not visited[wi][wj][dir][cuts]:
                visited[wi][wj][dir][cuts] = 1
                q.append((wi, wj, dir, cuts, ops + 1))
            elif cell == 'T' and cuts < K and not visited[wi][wj][dir][cuts + 1]:
                visited[wi][wj][dir][cuts + 1] = 1
                q.append((wi, wj, dir, cuts + 1, ops + 1))
        # 좌회전
        ndir = (dir + 3) % 4
        if not visited[i][j][ndir][cuts]:
            visited[i][j][ndir][cuts] = 1
            q.append((i, j, ndir, cuts, ops + 1))
        # 우회전
        ndir = (dir + 1) % 4
        if not visited[i][j][ndir][cuts]:
            visited[i][j][ndir][cuts] = 1
            q.append((i, j, ndir, cuts, ops + 1))
    return -1

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = []
    for i in range(N):
        row = input().strip()
        for j in range(N):
            if row[j] == 'X':
                si, sj = i, j
            elif row[j] == 'Y':
                ei, ej = i, j
        grid.append(row)
    print(f"#{tc} {bfs()}")