from collections import deque
import sys
input=sys.stdin.readline
dir=((1,0),(-1,0),(0,1),(0,-1))
N,K = map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))
visited=[[0]*N for _ in range(N)]
t,x,y=map(int,input().split())
q=deque()
for virus in range(1,K+1):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == virus:
                q.append((i,j))
                visited[i][j]=1
while q:
    ti,tj=q.popleft()
    for d in dir:
        wi,wj=ti+d[0],tj+d[1]
        if 0<=wi<N and 0<=wj<N and not visited[wi][wj] and not grid[wi][wj] and visited[ti][tj]+1<t+2:
            visited[wi][wj]=visited[ti][tj]+1
            grid[wi][wj]=grid[ti][tj]
            q.append((wi,wj))
print(grid[x-1][y-1])

