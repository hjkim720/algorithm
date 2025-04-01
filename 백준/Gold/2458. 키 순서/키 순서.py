from collections import deque
import sys
input=sys.stdin.readline
def bfs(s,arr):
    cnt=0
    q=deque()
    q.append(s)
    visited=[0]*(N+1)
    visited[s]=1
    while q:
        t=q.popleft()
        for child in arr[t]:
            if not visited[child]:
                q.append(child)
                visited[child]=1
                cnt+=1
    return cnt
N,M=map(int,input().split())
graph_1=[[] for _ in range(N+1)]
graph_2=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    graph_1[u].append(v)
    graph_2[v].append(u)
res=0
for i in range(1,N+1):
    if bfs(i,graph_1)+bfs(i,graph_2)==N-1:
        res+=1
print(res)