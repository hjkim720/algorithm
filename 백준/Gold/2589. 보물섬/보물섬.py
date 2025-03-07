from collections import deque
dir=((1,0),(0,1),(-1,0),(0,-1))
def bfs(si,sj):
    global max_len
    q=deque()
    q.append((si,sj))
    visited=[[0]*M for _ in range(N)]
    visited[si][sj]=1
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and island[wi][wj]=='L' and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+1
    tmp_max=max(map(max,visited))
    if tmp_max>max_len:
        max_len=tmp_max



N,M=map(int,input().split())
island=[list(map(str,input())) for _ in range(N)]
max_len=0
for i in range(N):
    for j in range(M):
        if island[i][j]=='L':
            bfs(i,j)
print(max_len-1)
