import sys
from collections import deque
input=sys.stdin.readline
dir = [(1,0), (0,1), (-1,0), (0,-1)]
jump = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]

def bfs():
    q = deque()
    q.append((0, 0, 0, 0))
    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = 1

    while q:
        ti, tj, k, cnt = q.popleft()
        if (ti,tj)==(H-1,W-1):
            return cnt
      
        for d in dir:
            wi, wj = ti+d[0], tj+d[1]
            if 0<=wi<H and 0<=wj<W and grid[wi][wj]==0 and not visited[wi][wj][k]:
                visited[wi][wj][k] = 1
                q.append((wi, wj, k, cnt+1))
       
        if k < K:
            for 짬프 in jump:
                wi, wj = ti+짬프[0], tj+짬프[1]
                if 0<=wi<H and 0<=wj<W and grid[wi][wj]==0 and not visited[wi][wj][k+1]:
                    visited[wi][wj][k+1] = 1
                    q.append((wi, wj, k+1, cnt+1))
    return -1
K=int(input())
W,H=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(H))
print(bfs())