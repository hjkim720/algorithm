from collections import deque
def bfs():
    q=deque()
    q.append(0)
    visited=[1000000000000]*(N+1)
    visited[0]=0
    while q:
        t=q.popleft()
        for i in range(1,lst[t]+1):
            w=t+i
            if w>=N-1:
                return visited[t]+1
            if visited[w]>visited[t]+1:
                visited[w]=visited[t]+1
                q.append(w)
    return -1


N=int(input())
lst=list(map(int,input().split()))
if N==1:
    print(0)
else:
    print(bfs())