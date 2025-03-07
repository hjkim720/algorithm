from collections import deque
dir=((1,0),(0,1),(-1,0),(0,-1))
def bfs():
    q=deque()
    visited=[[0]*M for _ in range(N)]
    q.append((0,0))
    visited[0][0]=1
    while q:
        ti,tj=q.popleft()
        if (ti,tj)==(N-1,M-1):
            return visited[ti][tj]
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and lst[wi][wj]==1 and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+1


N,M=map(int,input().split())
lst=[list(map(int,input())) for _ in range(N)]
print(bfs())