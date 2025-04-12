from collections import deque
dir=((1,0),(0,1),(0,-1),(-1,0))
def bfs():
    q=deque()
    q.append((0,0,0))
    visited=[[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0]=1
    while q:
        ti,tj,broken=q.popleft()
        if (ti,tj)==(N-1,M-1):
            return visited[ti][tj][broken]
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M:
                if grid[wi][wj]==0 and visited[wi][wj][broken]==0:
                    visited[wi][wj][broken]=visited[ti][tj][broken]+1
                    q.append((wi,wj,broken))
                elif grid[wi][wj]==1 and broken<K and visited[wi][wj][broken+1]==0:
                    visited[wi][wj][broken+1]=visited[ti][tj][broken]+1
                    q.append((wi,wj,broken+1))
    return -1
N,M,K=map(int,input().split())
grid = list(list(map(int,input().strip())) for _ in range(N))
print(bfs())