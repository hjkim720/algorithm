from collections import deque
import sys
input=sys.stdin.readline
dir=((1,-1),(1,1),(1,2),(1,-2))
def bfs(start_loc):
    q=deque()
    q.append((0,start_loc))
    visited=[[21e9]*3 for _ in range(N)]
    visited[0][start_loc]=lst[0][start_loc]
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if wi == N - 1:
                if 0<=wi<N and 0<=wj<3 and visited[wi][wj]>visited[ti][tj]+lst[wi][wj] and wj != start_loc:
                    visited[wi][wj]=visited[ti][tj]+lst[wi][wj]
                    q.append((wi,wj))
            else:
                if 0<=wi<N and 0<=wj<3 and visited[wi][wj]>visited[ti][tj]+lst[wi][wj]:
                    visited[wi][wj]=visited[ti][tj]+lst[wi][wj]
                    q.append((wi,wj))

    return min(visited[N-1])


N = int(input())
lst=list(list(map(int,input().split())) for _ in range(N))
res=21e9
for i in range(3):
    res=min(res,bfs(i))
print(res)