from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs():
    q=deque()
    q.append((0,0))
    visited=[[float('inf')]*N for _ in range(N)]
    visited[0][0]=0
    while q:
        ti,tj=q.popleft()
 
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<N and visited[wi][wj]>visited[ti][tj]+arr[wi][wj]:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+arr[wi][wj]
    return visited
 
 
T=int(input())
for testcase in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    print(f'#{testcase} {bfs()[N-1][N-1]}')