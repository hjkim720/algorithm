from collections import deque
def bfs():
    q=deque()
    q.append(s)
    visited=[-1]*(N+1)
    visited[s]=0
    while q:
        t=q.popleft()
        if t == e:
            return visited[t]
        for items in graph[t]:
            node=items[0]
            dist=items[1]
            if visited[node]==-1:
                visited[node]=visited[t]+dist
                q.append(node)
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,d=map(int,input().split())
    graph[u].append((v,d))
    graph[v].append((u,d))
for _ in range(M):
    s,e=map(int,input().split())
    print(bfs())