import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    dist = [[] for _ in range(N + 1)]
    heapq.heappush(dist[1], 0)
    while q:
        cost, cur = heapq.heappop(q)
        for nxt, weight in graph[cur]:
            nxt_cost=cost+weight
            if len(dist[nxt])<K:
                heapq.heappush(dist[nxt],-nxt_cost)
                heapq.heappush(q,(nxt_cost,nxt))
            elif -dist[nxt][0]>nxt_cost:
                heapq.heappop(dist[nxt])
                heapq.heappush(dist[nxt],-nxt_cost)
                heapq.heappush(q,(nxt_cost,nxt))
    for i in range(1,N+1):
        print(-dist[i][0] if len(dist[i])==K else -1)

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
dijkstra()
