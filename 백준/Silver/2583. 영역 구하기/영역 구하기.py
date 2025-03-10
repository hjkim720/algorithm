from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs(si,sj):
    global sizes,visited
    size=1
    q=deque()
    q.append((si,sj))
    visited[si][sj]=1
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<M and 0<=wj<N and grid[wi][wj]==0 and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=1
                size+=1
    sizes.append(size)


M, N, K = map(int, input().split())
grid = [[0] * N for _ in range(M)]
sizes=[]
cnt=0
visited=[[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(M - y1 - 1, M - y2 - 1, -1):
            grid[j][i] = 1
for i in range(M):
    for j in range(N):
        if grid[i][j]==0 and visited[i][j]==0:
            bfs(i,j)
            cnt+=1
sizes.sort()
print(cnt)
print(*sizes)
