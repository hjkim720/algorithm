from collections import deque
dir=((1,0),(0,1),(-1,0),(0,-1))
def bfs(si,sj):
    global visited
    cnt=1
    q=deque()
    q.append((si,sj))
    visited[si][sj]=gcnt
    while q:
        ti,tj=q.popleft()
        for di, dj in dir:
            wi,wj=ti+di,tj+dj
            if 0<=wi<N and 0<=wj<M and grid[wi][wj]==0 and visited[wi][wj]==0: 
                q.append((wi,wj))
                visited[wi][wj]=gcnt
                cnt+=1
    return cnt
N,M=map(int,input().split())
grid=[list(map(int,input().strip())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
gcnt=0
dic={}
walls=[]
for i in range(N):
    for j in range(M):
        if grid[i][j]==0 and not visited[i][j]:
            gcnt+=1
            dic[gcnt]=bfs(i,j)
        if grid[i][j]==1:
            walls.append((i,j))

for ti, tj in walls:
    flag=set()
    for di,dj in dir:
        wi,wj=ti+di,tj+dj
        if 0<=wi<N and 0<=wj<M and visited[wi][wj] and visited[wi][wj] not in flag:
            tmp=visited[wi][wj]
            grid[ti][tj]+=dic[tmp]
            grid[ti][tj]%=10
            flag.add(tmp)
for row in grid:
    print(*row,sep='')