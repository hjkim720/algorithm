from collections import deque
dir=((2,-1),
   (2,1),
   (-2,1),
   (-2,-1),
   (-1,-2),
   (1,-2),
   (-1,2),
   (1,2))
def bfs():
    q=deque()
    visited=[[0]*N for _ in range(N)]
    q.append((si,sj))
    visited[si][sj]=1
    while q:
        ti,tj=q.popleft()
        if ti==ei and tj==ej:
            return visited[ti][tj]-1
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<N and visited[wi][wj]<visited[ti][tj]+1:
                visited[wi][wj]=visited[ti][tj]+1
                q.append((wi,wj))
T=int(input())
for testcase in range(1,T+1):
    N=int(input())
    grid=[[0]*N for _ in range(N)]

    si,sj=map(int,input().split())
    ei,ej=map(int,input().split())
    print(bfs())