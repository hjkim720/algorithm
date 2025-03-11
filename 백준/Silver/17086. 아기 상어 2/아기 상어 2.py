from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
def bfs(si,sj):
    q=deque()
    q.append((si,sj))
    visited=[[0]*M for _ in range(N)]
    visited[si][sj]=1
    while q:
        ti,tj=q.popleft()
        if grid[ti][tj]==1:
            return visited[ti][tj]-1
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+1

N,M = map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
res=0
for i in range(N):
    for j in range(M):
        if grid[i][j]==0:
            dist=bfs(i,j)
            if dist>res:
                res=dist
print(res)