from collections import deque
def bfs():
    q=deque()
    q.append((0,0))
    visited=[[0]*N for _ in range(M)]
    visited[0][0]=1
    while q:
        ti,tj=q.popleft()
        if (ti,tj)==(M-1,N-1):
            return 'Yes'
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<M and 0<=wj<N and not visited[wi][wj] and grid[wi][wj]:
                visited[wi][wj]=1
                q.append((wi,wj))
    return 'No'
dir = ((1,0),(0,1))
N, M = map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(M)]
print(bfs())