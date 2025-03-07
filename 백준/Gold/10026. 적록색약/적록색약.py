from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs(coord,color):
    global cnt
    c=color
    q=deque()
    q.append(coord)
    visited=[[0]*N for _ in range(N)]
    visited[coord[0]][coord[1]]=1
    ori[coord[0]][coord[1]]=cnt
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<N and ori[wi][wj]==c and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=1
                ori[wi][wj]=cnt
    cnt+=1
def bfs2(coord,color):
    global cnt2
    c=color
    q=deque()
    q.append(coord)
    visited=[[0]*N for _ in range(N)]
    visited[coord[0]][coord[1]]=1
    blind[coord[0]][coord[1]]=cnt
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if c == 'R' or c=='G':
                if 0<=wi<N and 0<=wj<N and blind[wi][wj] in ('R','G') and visited[wi][wj]==0:
                    q.append((wi,wj))
                    visited[wi][wj]=1
                    blind[wi][wj]=cnt2
            else:
                if 0<=wi<N and 0<=wj<N and blind[wi][wj]=='B' and visited[wi][wj]==0:
                    q.append((wi,wj))
                    visited[wi][wj]=1
                    blind[wi][wj]=cnt2
    cnt2+=1


N=int(input())
lst=[list(map(str,input())) for _ in range(N)]
cnt=1
cnt2=1
ori=[row[:] for row in lst]
blind=[row[:] for row in lst]
for i in range(N):
    for j in range(N):
        if ori[i][j] in ('R','G','B'):
            bfs((i,j),lst[i][j])
        if blind[i][j] in ('R','G','B'):
            bfs2((i,j),lst[i][j])

print(cnt-1)
print(cnt2-1)
           


