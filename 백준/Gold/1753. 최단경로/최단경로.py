import heapq
import sys
input=sys.stdin.readline
def dijkstra(start_node):
    pq = [(0, start_node)]  # (누적거리, 노드번호)
    dists = [float('inf')] * (N+1) # 각 정점까지의 최단거리를 저장할 리스트
    dists[start_node] = 0  # 시작노드 최단 거리는 0
    while pq:
        dist, node = heapq.heappop(pq)
        # 이미 더 작은 경로로 온 적이 있다면 pass
        if dists[node] < dist:
            continue
        for next_info in graph[node]:
            next_dist = next_info[0]  # 다음 노드로 가기 위한 가중치
            next_node = next_info[1]  # 다음 노드 번호
            # 다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist

            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면 continue
            if dists[next_node] <= new_dist:
                continue
            # next_node 까지 도착하는 데 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return dists
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
K=int(input())
for _ in range(M):
    s,e,w=map(int,input().split())
    graph[s].append((w,e))
res=dijkstra(K)
for i in range(1,len(res)):
    if res[i]== float('inf'):
        print('INF')
    else:
        print(res[i])