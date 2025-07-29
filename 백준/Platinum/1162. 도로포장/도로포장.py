import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1, 0)) # (cost,n,k)
    visited = [[21e9]*(K+1) for _ in range(N+1) ]
    visited[1][0] = 0
    while q:
        cost, cur, k = heapq.heappop(q)
        if cur == N:
            return cost
        if visited[cur][k] < cost:
            continue
        for nxt, weight in graph[cur]:
            if visited[nxt][k] > cost + weight:
                visited[nxt][k] = cost + weight
                heapq.heappush(q, (cost + weight, nxt, k))
            if k < K and visited[nxt][k+1] > cost:
                visited[nxt][k+1] = cost
                heapq.heappush(q, (cost, nxt, k+1))

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
print(dijkstra())
