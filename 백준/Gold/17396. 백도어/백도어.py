'''
제가 트런들을 좀 하긴하는데 힙큐를 싫어해요
'''
import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
ward = list(map(int, input().split()))        
graph = [[] for _ in range(V)]                 

for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dijkstra():
    dist = [21e9] * V
    q   = []
    dist[0] = 0
    heapq.heappush(q, (0, 0))                

    while q:
        cur_cost, cur = heapq.heappop(q)
        if cur_cost > dist[cur]:
            continue
        if cur == V - 1:
            return cur_cost

        for nxt, weight in graph[cur]:
            if ward[nxt] and nxt != V - 1:    
                continue                       
            nxt_cost = cur_cost + weight
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

    return -1                                 

print(dijkstra())
