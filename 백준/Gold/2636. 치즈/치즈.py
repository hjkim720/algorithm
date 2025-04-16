from collections import deque
import sys
input=sys.stdin.readline
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs():
    tmp=[]
    q=deque()
    q.append((0,0))
    visited=[[0]*M for _ in range(N)]
    visited[0][0]=1
    while q:
        ti,tj=q.popleft()
        if grid[ti][tj]==1:
            tmp.append((ti,tj))
            continue
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and not visited[wi][wj]:
                q.append((wi,wj))
                visited[wi][wj]=1
    return tmp

N,M=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))
cnt=0
will_melt=[]
while True:
    tmp=bfs()
    if not tmp:
        break
    will_melt.append(tmp)
    for coords in will_melt[-1]:
        i,j=coords[0],coords[1]
        grid[i][j]=0
print(len(will_melt))
print(len(will_melt[-1]))
