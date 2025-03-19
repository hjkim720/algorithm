from collections import deque

dir = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_end():
    flag=False
    end = 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 3:
                end = (i, j)
                flag = True
        if flag:
            break
    return end


def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [[0] * 100 for _ in range(100)]
    visited[start[0]][start[1]] = 1
    while q:
        ti, tj = q.popleft()
        if (ti, tj) == end:
            return 1
        for d in dir:
            wi, wj = ti + d[0], tj + d[1]
            if 0 <= wi < 100 and 0 <= wj < 100 and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = 1
    return 0


for testcase in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    start, end = (1,1),find_end()
    print(f'#{testcase} {bfs(start, end)}')