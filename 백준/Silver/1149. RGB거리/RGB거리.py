from collections import deque
def bfs(s):
    q=deque()
    q.append((0,s))
    visited=[[float('inf')]*3 for _ in range(N)]
    visited[0][s]=lst[0][s]
    dir=((1,1),(1,-1),(1,-2),(1,2))
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<3 and visited[wi][wj]>visited[ti][tj]+lst[wi][wj]:
                visited[wi][wj]=visited[ti][tj]+lst[wi][wj]
                q.append((wi,wj))
    return min(visited[-1][:])
N=int(input())
lst=list(list(map(int,input().split())) for _ in range(N))
res=1000000000
for i in range(3):
    res=min(res,bfs(i))
print(res)