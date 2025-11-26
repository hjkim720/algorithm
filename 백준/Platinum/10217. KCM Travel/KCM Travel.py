from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for i in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    for edge in graph:
        edge.sort(key=lambda x: x[2])
    visited = [[21e9] * (M + 1) for _ in range(N + 1)]
    visited[1][0] = 0
    q = deque()
    q.append((1, 0, 0))

    while q:
        node, cost, time = q.popleft()
        if time > visited[node][cost]:
            continue
        for v, c, d in graph[node]:
            ncost = cost + c
            if ncost > M:
                continue
            ntime = time + d
            if ntime < visited[v][ncost]:
                for cc in range(ncost, M + 1):
                    if ntime < visited[v][cc]:
                        visited[v][cc] = ntime
                    else:
                        break
                q.append((v, ncost, ntime))

    ans = min(visited[N])
    print(ans if ans != 21e9 else "Poor KCM")
