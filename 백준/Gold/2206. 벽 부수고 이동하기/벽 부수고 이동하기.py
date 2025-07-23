N,M=map(int,input().split())
maze=[list(map(int,input())) for _ in range(N)]
dir=[[1,0],[-1,0],[0,1],[0,-1]]
dir2=[[1,1],[-1,-1],[1,-1],[-1,1]]
flag=0
def bfs_start(n,m,dir):
    global flag
    visited=[[0]*m for _ in range(n)]
    q=[[0,0]]
    visited[0][0]=1
    nobreak=10000000
    while q:
        ti,tj=q.pop(0)
        if (ti,tj)==(N-1,M-1):
            nobreak= visited[ti][tj]
            flag=1
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and maze[wi][wj]==0 and visited[wi][wj]==0:
                q.append([wi,wj])
                visited[wi][wj]=visited[ti][tj]+1
    return visited,nobreak
def bfs_end(n,m,dir):
    visited=[[0]*m for _ in range(n)]
    q=[[n-1,m-1]]
    visited[n-1][m-1]=1
    while q:
        ti,tj=q.pop(0)
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and maze[wi][wj]==0 and visited[wi][wj]==0:
                q.append([wi,wj])
                visited[wi][wj]=visited[ti][tj]+1
    return visited
from_start,nobreak=bfs_start(N,M,dir)
from_end=bfs_end(N,M,dir)
res=[nobreak]
for i in range(N):
    for j in range(M):
        if from_start[i][j]!=0:
            for d in dir:
                xi,xj=i+2*d[0],j+2*d[1]
                if 0<=xi<N and 0<=xj<M and from_end[xi][xj] !=0:
                    res.append(from_start[i][j]+from_end[xi][xj]+1)
            for d2 in dir2:
                zi,zj=i+d2[0],j+d2[1]
                if 0<=zi<N and 0<=zj<M and from_end[zi][zj] !=0:
                    res.append(from_start[i][j]+from_end[zi][zj]+1)
if res == [10000000]:
    print(-1)
else:
    print(min(res))