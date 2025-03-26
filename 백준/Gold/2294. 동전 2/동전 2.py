from collections import deque
import sys
input=sys.stdin.readline
def bfs():
    q=deque()
    q.append(0)
    visited=[K+1]*(K+1)
    visited[0]=0
    while q:
        t=q.popleft()
        if t==K:
            return visited[t]
        for coin in coins:
            w=t+coin
            if w<=K and visited[w]>visited[t]+1:
                visited[w]=visited[t]+1
                q.append(w)
    return -1

N,K=map(int,input().split())
coins=[int(input()) for _ in range(N)]
print(bfs())
