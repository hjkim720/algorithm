from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs(si,sj,sink):
    global visited
    q = deque() 
    q.append((si,sj))
    visited[si][sj]=1
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<N and town[wi][wj]>sink and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=1
                
N=int(input())
town=[list(map(int,input().split())) for _ in range(N)]
highest=max(map(max,town))
res=1
for rain_amount in range(1,highest):
    visited=[[0]*N for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if town[i][j]>rain_amount and visited[i][j]==0:
                cnt+=1
                bfs(i,j,rain_amount)
    if cnt>res:
        res=cnt
print(res)
