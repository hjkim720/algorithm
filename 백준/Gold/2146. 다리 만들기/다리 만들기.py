import sys
from collections import deque
input=sys.stdin.readline
dir=((1,0),(-1,0),(0,1),(0,-1))
def group_island(coord):
    global visited,group_num,shore
    group_num+=1
    q=deque()
    q.append(coord)
    visited[coord[0]][coord[1]]=1
    grid[coord[0]][coord[1]]=group_num
    while q:
         ti,tj=q.popleft()
         for d in dir:
                wi,wj=ti+d[0],tj+d[1]
                if 0<=wi<N and 0<=wj<N and grid[wi][wj]==1 and not visited[wi][wj]:
                   q.append((wi,wj))
                   visited[wi][wj]=1
                   grid[wi][wj]=group_num
                elif 0<=wi<N and 0<=wj<N and grid[wi][wj]==0:
                   shore.add((wi,wj,group_num))
def bfs(info):
    si,sj,gn=info[0],info[1],info[2]
    v=[[0]*N for _ in range(N)]
    q=deque()
    q.append((si,sj))
    v[si][sj]=1
    while q:
         ti,tj=q.popleft()
         if v[ti][tj]>res:
              return 100000000
         if grid[ti][tj]!=0 and grid[ti][tj]!=gn:
              return v[ti][tj]
         for d in dir:
                wi,wj=ti+d[0],tj+d[1]
                if 0<=wi<N and 0<=wj<N and grid[wi][wj]!=gn and not v[wi][wj]:
                   q.append((wi,wj))
                   v[wi][wj]=v[ti][tj]+1
    return 1000000
N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
res=10000000
shore=set()
group_num=1
visited=[[0]*N for _ in range(N)]
for i in range(N):
        for j in range(N):
            if grid[i][j]==1 and not visited[i][j]:
                group_island((i,j))
for items in shore:
     r=bfs(items)
     if r<res:
          res=r
print(res-1)