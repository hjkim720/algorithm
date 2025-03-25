from collections import deque
def bfs():
    q=deque()
    q.append(N)
    visited=[100001]*100001
    previous=[-1]*100001
    visited[N]=0
    while q:
        t=q.popleft()
        if t==K:
            res=visited[t]
            route=[]
            while t!=-1:
                route.append(t)
                t=previous[t]
            return res, route[::-1]
        w=t+1
        if 0<=w<=100000 and visited[w]>visited[t]+1:
            q.append(w)
            visited[w]=visited[t]+1
            previous[w]=t
        w=t-1
        if 0<=w<=100000 and visited[w]>visited[t]+1:
            q.append(w)
            visited[w]=visited[t]+1
            previous[w]=t
        w=2*t
        if 0<=w<=100000 and visited[w]>visited[t]+1:
            q.append(w)
            visited[w]=visited[t]+1
            previous[w]=t

N,K=map(int,input().split())
min_len,path=bfs()
print(min_len)
print(*path)