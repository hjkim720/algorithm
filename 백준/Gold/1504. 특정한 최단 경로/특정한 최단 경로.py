import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    dist = [21e9] * (V+1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for nxt, w in graph[now]:
            if dist[nxt] > cost + w:
                dist[nxt] = cost + w
                heapq.heappush(q, (dist[nxt], nxt))
    return dist

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, input().split())

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[V]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[V]

res = min(path1, path2)
print(res if res < 21e9 else -1)
