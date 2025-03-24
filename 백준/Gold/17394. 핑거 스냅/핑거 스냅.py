from collections import deque
from math import sqrt
def is_prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def bfs():
    q=deque()
    q.append(N)
    visited=[100000]*1000001
    visited[N]=0
    while q:
        t=q.popleft()
        if A<=t<=B and is_prime(t):
            return visited[t]
        w=t//3
        if 0 <= w <= 1000000 and visited[w]>visited[t]+1:
            q.append(w)
            visited[w]=visited[t]+1
        w=t//2
        if 0 <= w <= 1000000 and visited[w]>visited[t]+1:
            q.append(w)
            visited[w]=visited[t]+1
        w=t+1
        if 0 <= w <= 1000000 and visited[w]>visited[t]+1:
            q.append(w)
            visited[w]=visited[t]+1
        w=t-1
        if 0 <= w <= 1000000 and visited[w]>visited[t]+1:
            q.append(w)
            visited[w]=visited[t]+1
    return -1


T=int(input())
for tc in range(T):
    N,A,B=map(int,input().split())
    print(bfs())