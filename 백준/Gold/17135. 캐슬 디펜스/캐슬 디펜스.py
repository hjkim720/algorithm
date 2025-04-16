from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline
def bfs():
    global temp_grid
    q = deque()
    q.append((len(temp_grid)-1,case))
    visited=[[0]*M for _ in range(len(grid))]
    visited[len(temp_grid)-1][case]=1
    tmp=0
    while q:
        ti, tj = q.popleft()
        if temp_grid[ti][tj]==1 and 0<visited[ti][tj]<D+2:
            tmp=(ti,tj)
            return tmp
        for d in dir:
            wi, wj = ti + d[0], tj + d[1]
            if 0 <= wi < len(temp_grid) and 0 <= wj < M and not visited[wi][wj]:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+1
    return tmp

dir=((0,-1),(-1,0),(0,1))
N,M,D=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))
grid+=[[0]*M]
ans=0
for cases in combinations(range(M),3):
    temp_grid=[row[:] for row in grid]
    res=[]
    while temp_grid:
        will_die=set()
        if len(temp_grid)==1:
            break
        for case in cases:
            tmp=bfs()
            if tmp:
                will_die.add(tmp)
        for dead in will_die:
            temp_grid[dead[0]][dead[1]]=0
            res.append(dead)
        temp_grid.pop(-2)
    ans=max(len(res),ans)
print(ans)