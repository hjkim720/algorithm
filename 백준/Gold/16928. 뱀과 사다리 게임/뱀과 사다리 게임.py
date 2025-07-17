from collections import deque
import sys
input=sys.stdin.readline
def bfs():
    q=deque()
    q.append((1,0))
    visited=[0]*101
    visited[1]=1
    while q:
        loc,cnt=q.popleft()
        if loc in ladders:
            loc=ladders[loc]
        if loc in snakes:
            loc=snakes[loc]
        if loc==100:
            return cnt
        for dice in range(1,7):
            nxt=loc+dice
            if nxt<=100 and not visited[nxt]:
                visited[nxt]=1
                q.append((nxt,cnt+1))

N, M = map(int,input().split())
ladders={}
snakes={}
for _ in range(N):
    s,e=map(int,input().split())
    ladders[s]=e
for _ in range(M):
    s,e=map(int,input().split())
    snakes[s]=e
print(bfs())