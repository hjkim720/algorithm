import sys
from collections import deque
input=sys.stdin.readline
def f_bfs():
    global fire_visited
    for coords in fire_lst:
        fire_visited[coords[0]][coords[1]]=1
    while fire_lst:
        ti,tj=fire_lst.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and grid[wi][wj]!='#' and fire_visited[wi][wj]==0:
                fire_lst.append((wi,wj))
                fire_visited[wi][wj]=fire_visited[ti][tj]+1
def bfs(start_loc,fire_visited):
    q=deque()
    q.append((start_loc[0],start_loc[1]))
    visited=[[0]*M for _ in range(N)]
    visited[start_loc[0]][start_loc[1]]=1
    while q:
        ti,tj=q.popleft()
        if ti==0 or ti==N-1 or tj==0 or tj==M-1:
            return visited[ti][tj]
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and grid[wi][wj]!='#' and not visited[wi][wj]:
                if fire_visited[wi][wj]!=0:
                    if fire_visited[wi][wj]>visited[ti][tj]+1:
                        q.append((wi,wj))
                        visited[wi][wj]=visited[ti][tj]+1
                else:
                    q.append((wi,wj))
                    visited[wi][wj]=visited[ti][tj]+1

    return 'IMPOSSIBLE'
T=int(input())
for tc in range(T):
    M,N=map(int,input().split())
    grid=[list(map(str,input())) for _ in range(N)]
    fire_lst=deque()
    start_loc=[0,0]
    dir=((1,0),(0,1),(-1,0),(0,-1))
    fire_visited=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j]=='*':
                fire_lst.append((i,j))
            elif grid[i][j]=='@':
                start_loc=[i,j]


    f_bfs()
    print(bfs(start_loc,fire_visited))