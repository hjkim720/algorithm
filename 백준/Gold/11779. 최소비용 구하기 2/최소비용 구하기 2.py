import heapq
import sys
input=sys.stdin.readline
def dijkstra():
    q=[(0,beg,[beg])]
    dist=[21e9]*(n+1)
    dist[beg]=0
    while q:
        cost,cur,path=heapq.heappop(q)
        if cur==tar:
            return dist[tar], path
        if cost>dist[cur]:
            continue
        for nxt,weight in graph[cur]:
            if dist[cur]+weight<dist[nxt]:
                dist[nxt]=dist[cur]+weight
                heapq.heappush(q,(cost+weight,nxt,path+[nxt]))
n= int(input())
m = int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,input().split())
    graph[s].append((e,w))
beg,tar=map(int,input().split())
res,path=dijkstra()
print(res)
print(len(path))
print(*path)