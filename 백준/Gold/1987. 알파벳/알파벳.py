import sys
input = sys.stdin.readline
dir = ((1, 0), (-1, 0), (0, 1), (0, -1))

def dfs(i, j, visited):
    max_count = 1  # 현재 위치부터 시작
    for dx, dy in dir:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] not in visited:
            visited.add(grid[ni][nj])  # 방문 처리
            max_count = max(max_count, 1 + dfs(ni, nj, visited))
            visited.remove(grid[ni][nj])  # 백트래킹
    return max_count
N, M = map(int, input().split())
grid = [list(map(str,input())) for _ in range(N)]
print(dfs(0, 0, set(grid[0][0])))
