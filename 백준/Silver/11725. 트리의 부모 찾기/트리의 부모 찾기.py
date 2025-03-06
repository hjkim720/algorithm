from collections import deque
def bfs():
    q=deque()
    visited=[0]*(N+1)
    q.append(1)
    visited[1]=1
    while q:
        t=q.popleft()
        for child in graph[t]:
            if visited[child]==0:
                q.append(child)
                visited[child]=1
                tree[child].append(t)
N=int(input())
graph=[[] for _ in range(N+1)]
tree=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs()
for i in range(2,N+1):
    print(*tree[i])