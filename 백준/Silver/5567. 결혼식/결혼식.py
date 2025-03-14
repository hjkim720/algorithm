from collections import deque
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
def bfs():
    q=deque()
    q.append(1)
    visited=[0]*(N+1)
    visited[1]=1
    while q:
        t=q.popleft()
        for items in graph[t]:
            if not visited[items] and visited[t]<=2:
                q.append(items)
                visited[items]=visited[t]+1
    cnt=0
    for i in visited[2:]:
        if i !=0:
            cnt+=1
    return cnt
print(bfs())