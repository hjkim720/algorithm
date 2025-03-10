import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a,b=map(int,input().split())
M=int(input())
graph=[[] for _ in range(N+1)]

for i in range(M):
    p,c=map(int,input().split())
    graph[c].append(p)
 
    graph[p].append(c)

q=deque()
q.append(a)
visited=[0]*(N+1)
visited[a]=1
while q:
    tmp=q.popleft()
    if tmp==b:
        print(visited[b]-1)
        break
    for items in graph[tmp]:
        if visited[items]==0:
            q.append(items)
            visited[items]=visited[tmp]+1
else:
    print(-1)
