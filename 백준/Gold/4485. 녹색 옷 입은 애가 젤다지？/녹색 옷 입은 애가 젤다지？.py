from collections import deque
import sys
input=sys.stdin.readline
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs():
    q=deque()
    q.append((0,0))
    visited=[[21e9]*N for _ in range(N)]
    visited[0][0]=grid[0][0]
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<N and visited[wi][wj]>visited[ti][tj]+grid[wi][wj]:
                visited[wi][wj]=visited[ti][tj]+grid[wi][wj]
                q.append((wi,wj))
    return visited[N-1][N-1]

tc=0
while True:
   N=int(input())
   if N==0:
      break
   else:
      tc+=1
      grid=list(list(map(int,input().split())) for _ in range(N))
      print(f'Problem {tc}: {bfs()}')