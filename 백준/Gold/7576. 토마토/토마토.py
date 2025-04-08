import sys
from collections import deque
input=sys.stdin.readline
M,N=map(int,input().split())
boxes=[list(map(int,input().split())) for _ in range(N)]

q=deque()
def find_ripe():
    for i in range(N):
        for j in range(M):
            if boxes[i][j]==1:
                q.append([i,j])
    return q
def bfs(q):
    dir=[[1,0],[-1,0],[0,1],[0,-1]]
    visited=[[0]*M for _ in range(N)]
    for tomato in q:
        visited[tomato[0]][tomato[1]]=1
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and boxes[wi][wj]==0 and visited[wi][wj]==0:
                q.append([wi,wj])
                visited[wi][wj]=visited[ti][tj]+1
                boxes[wi][wj]=1
    days=visited[0][0]
    for i in range(N):
        for j in range(M):
            if visited[i][j]>days:
                days=visited[i][j]
            if boxes[i][j]==0:
                return -1
    return days-1
print(bfs(find_ripe()))