from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs(coord):
    q=deque()
    q.append(coord)
    visited=[[0]*M for _ in range(N)]
    visited[0][0]=0
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and lst[wi][wj]==1 and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+1
    return visited

N,M=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]

is_found=False
for i in range(N):
    for j in range(M):
        if lst[i][j]==2:
            start=(i,j)

            is_found=True
            break
    if is_found:
        break

result=bfs(start)

for i in range(N):
    for j in range(M):
        if lst[i][j]==1 and result[i][j]==0:
            result[i][j]=-1


for rows in result:
    print(*rows)