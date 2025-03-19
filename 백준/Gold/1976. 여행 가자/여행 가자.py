from collections import deque
def bfs():
    q=deque()
    q.append(target[0])
    visited[target[0]]=1
    while q:
        t=q.popleft()
        for nodes in graph[t]:
            if not visited[nodes]:
                visited[nodes]=1
                q.append(nodes)
N=int(input())
M=int(input())
graph=[set() for _ in range(N)]
for i in range(N):
    lst=list(map(int,input().split()))
    for j in range(N):
        if lst[j]==1:
            graph[j].add(i)
            graph[i].add(j)
target=list(map(int,input().split()))
for i in range(M):
    target[i]=target[i]-1
visited=[0]*N
bfs()
res='YES'
for cities in target:
    if not visited[cities]:
        res='NO'
        break
print(res)