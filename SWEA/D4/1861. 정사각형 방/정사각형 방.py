from collections import deque
def bfs(si,sj):
    global res
    q=deque()
    q.append((si,sj))
    visited=[[0]*N for _ in range(N)]
    visited[si][sj]=1
    while q:
        ti,tj=q.popleft()
        tmp = (grid[si][sj], visited[ti][tj])
        for d in ((1,0),(0,1),(-1,0),(0,-1)):
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<N and grid[wi][wj]==grid[ti][tj]+1:
                visited[wi][wj]=visited[ti][tj]+1
                q.append((wi,wj))

    if tmp[1]==res[1]:
        if tmp[0]<res[0]:
            res=tmp[:]
    elif tmp[1]>res[1]:
        res=tmp[:]
    return




T=int(input())
for testcase in range(1,T+1):
    N=int(input())
    res=(float('inf'),0)
    grid=[list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    print(f'#{testcase}',end=' ')
    print(*res)